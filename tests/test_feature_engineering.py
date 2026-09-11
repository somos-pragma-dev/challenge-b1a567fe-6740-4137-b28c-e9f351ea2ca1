import pytest
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from typing import Dict, List, Tuple, Any


class TestFeatureEngineering:
    """Pruebas para validar que la ingeniería de características evita fuga de información."""

    @pytest.fixture
    def dataset_with_split(self) -> Dict[str, pd.DataFrame]:
        """Genera un dataset dividido en train y test."""
        np.random.seed(42)
        n_samples = 200
        
        data = {
            'edad': np.random.randint(18, 70, n_samples),
            'ingreso_mensual': np.random.uniform(1000, 15000, n_samples),
            'monto_prestamo': np.random.uniform(5000, 80000, n_samples),
            'plazo_meses': np.random.choice([12, 24, 36, 48, 60], n_samples),
            'historial_credito': np.random.randint(0, 6, n_samples),
            'score_credito': np.random.uniform(300, 850, n_samples),
            'estado_civil': np.random.choice(['soltero', 'casado', 'divorciado', 'viudo'], n_samples),
            'tipo_empleo': np.random.choice(['empleado', 'independiente', 'empresario', 'desempleado'], n_samples),
            'target': np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
        }
        
        df = pd.DataFrame(data)
        train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df['target'])
        
        return {'train': train_df.reset_index(drop=True), 'test': test_df.reset_index(drop=True)}

    @pytest.fixture
    def fitted_preprocessor(self) -> Tuple[ColumnTransformer, pd.DataFrame]:
        """Preprocesador ajustado solo con datos de entrenamiento."""
        np.random.seed(42)
        n_samples = 200
        
        train_data = pd.DataFrame({
            'edad': np.random.randint(18, 70, n_samples),
            'ingreso_mensual': np.random.uniform(1000, 15000, n_samples),
            'estado_civil': np.random.choice(['soltero', 'casado', 'divorciado'], n_samples),
            'tipo_empleo': np.random.choice(['empleado', 'independiente'], n_samples)
        })
        
        numeric_features = ['edad', 'ingreso_mensual']
        categorical_features = ['estado_civil', 'tipo_empleo']
        
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numeric_features),
                ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_features)
            ]
        )
        
        preprocessor.fit(train_data)
        
        return preprocessor, train_data

    def test_scaling_only_on_training_data(self, fitted_preprocessor: Tuple[ColumnTransformer, pd.DataFrame]) -> None:
        """Verifica que el escalado se ajuste solo con datos de entrenamiento."""
        preprocessor, train_data = fitted_preprocessor
        
        numeric_features = ['edad', 'ingreso_mensual']
        scaler = preprocessor.named_transformers_['num']
        
        # Verificar que scaler fue ajustado con datos de entrenamiento
        # Los parámetros mean_ y scale_ deben existir
        assert hasattr(scaler, 'mean_'), "Scaler no tiene atributo mean_"
        assert hasattr(scaler, 'scale_'), "Scaler no tiene atributo scale_"
        
        # Verificar que las medias calculadas son coherentes con datos de entrenamiento
        train_means = train_data[numeric_features].mean()
        for i, col in enumerate(numeric_features):
            assert np.isclose(scaler.mean_[i], train_means[col], rtol=0.01), (
                f"La media del scaler no corresponde a datos de entrenamiento para {col}"
            )

    def test_no_data_leakage_in_transform(self, dataset_with_split: Dict[str, pd.DataFrame]) -> None:
        """Verifica que no haya fuga de información al transformar datos de test."""
        train_df = dataset_with_split['train']
        test_df = dataset_with_split['test']
        
        numeric_features = ['edad', 'ingreso_mensual', 'monto_prestamo', 'score_credito']
        
        # Ajustar scaler solo con train
        scaler = StandardScaler()
        scaler.fit(train_df[numeric_features])
        
        # Transformar test con el scaler ajustado en train
        test_transformed = scaler.transform(test_df[numeric_features])
        
        # Verificar que los datos transformados no contain información de test
        # Los valores transformados de test deben estar en rangos similares a train
        train_transformed = scaler.transform(train_df[numeric_features])
        
        for i, col in enumerate(numeric_features):
            test_col = test_transformed[:, i]
            train_col = train_transformed[:, i]
            
            # Los valores transformados de test deben estar en el rango de train
            test_min_in_train = test_col.min() >= train_col.min() - 3 * train_col.std()
            test_max_in_train = test_col.max() <= train_col.max() + 3 * train_col.std()
            
            assert test_min_in_train and test_max_in_train, (
                f"Valores transformados de test para {col} están fuera del rango de train"
            )

    def test_onehot_encoding_consistency(self, fitted_preprocessor: Tuple[ColumnTransformer, pd.DataFrame]) -> None:
        """Verifica que la codificación one-hot sea consistente entre train y test."""
        preprocessor, train_data = fitted_preprocessor
        
        encoder = preprocessor.named_transformers_['cat']
        
        # Verificar que el encoder tiene categorías conocidas
        assert hasattr(encoder, 'categories_'), "Encoder no tiene categories_"
        
        # Verificar que todas las categorías de entrenamiento están presentes
        for i, cat_feature in enumerate(['estado_civil', 'tipo_empleo']):
            train_categories = set(train_data[cat_feature].unique())
            encoder_categories = set(encoder.categories_[i])
            assert train_categories.issubset(encoder_categories), (
                f"Categorías de entrenamiento no están en el encoder para {cat_feature}"
            )

    def test_no_target_leakage_in_features(self, dataset_with_split: Dict[str, pd.DataFrame]) -> None:
        """Verifica que las features no incluyan información del target."""
        train_df = dataset_with_split['train']
        
        feature_columns = [col for col in train_df.columns if col != 'target']
        
        # Verificar que ninguna feature tenga correlación perfecta con el target
        for col in feature_columns:
            if train_df[col].dtype in ['int64', 'float64']:
                correlation = train_df[col].corr(train_df['target'])
                # Una correlación de 1 o -1 indica filtración directa del target
                assert abs(correlation) < 0.99, (
                    f"Feature {col} tiene correlación {correlation:.3f} con target - posible filtración"
                )

    def test_train_test_separation_maintained(self, dataset_with_split: Dict[str, pd.DataFrame]) -> None:
        """Verifica que no haya overlap entre train y test."""
        train_df = dataset_with_split['train']
        test_df = dataset_with_split['test']
        
        # Crear una clave única para cada fila basada en todas las columns
        train_keys = train_df.apply(lambda x: tuple(x), axis=1)
        test_keys = test_df.apply(lambda x: tuple(x), axis=1)
        
        overlap = set(train_keys).intersection(set(test_keys))
        
        assert len(overlap) == 0, f"Se encontró overlap de {len(overlap)} filas entre train y test"

    def test_feature_engineering_reproducibility(self, dataset_with_split: Dict[str, pd.DataFrame]) -> None:
        """Verifica que la ingeniería de features sea reproducible."""
        train_df = dataset_with_split['train']
        
        numeric_features = ['edad', 'ingreso_mensual', 'monto_prestamo']
        
        # Ejecutar transformación dos veces
        scaler1 = StandardScaler()
        scaler1.fit(train_df[numeric_features])
        result1 = scaler1.transform(train_df[numeric_features])
        
        scaler2 = StandardScaler()
        scaler2.fit(train_df[numeric_features])
        result2 = scaler2.transform(train_df[numeric_features])
        
        # Los resultados deben ser idénticos
        np.testing.assert_array_almost_equal(
            result1, result2,
            err_msg="La transformación no es reproducible"
        )

    def test_numerical_stability_of_scaling(self, dataset_with_split: Dict[str, pd.DataFrame]) -> None:
        """Verifica estabilidad numérica del escalado con valores extremos."""
        train_df = dataset_with_split['train']
        
        # Agregar valores extremos para probar estabilidad
        extreme_data = train_df[['edad', 'ingreso_mensual']].copy()
        extreme_data.loc[len(extreme_data)] = [150, 1000000]  # Valores extremos
        
        scaler = StandardScaler()
        scaler.fit(extreme_data)
        
        # Verificar que no haya NaN o valores infinitos
        assert not np.isnan(scaler.mean_).any(), "Scaler mean contiene NaN"
        assert not np.isnan(scaler.scale_).any(), "Scaler scale contiene NaN"
        assert not np.isinf(scaler.mean_).any(), "Scaler mean contiene infinito"
        assert not np.isinf(scaler.scale_).any(), "Scaler scale contiene infinito"

    def test_categorical_encoding_no_unknown_categories(self, dataset_with_split: Dict[str, pd.DataFrame]) -> None:
        """Verifica que no haya categorías desconocidas en test que no estén en train."""
        train_df = dataset_with_split['train']
        test_df = dataset_with_split['test']
        
        categorical_features = ['estado_civil', 'tipo_empleo']
        
        for col in categorical_features:
            train_categories = set(train_df[col].unique())
            test_categories = set(test_df[col].unique())
            
            unknown_categories = test_categories - train_categories
            
            assert len(unknown_categories) == 0, (
                f"Categorías desconocidas en test para {col}: {unknown_categories}"
            )