"""
Módulo de ingeniería de características.

Este script crea nuevas variables, codifica variables categóricas, aplica
escalado y particiona los datos en conjuntos de entrenamiento, validación y prueba.
Evita la fuga de información mediante partición antes de cualquier transformación.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple, Dict, Optional, List
import logging
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class FeatureEngineer:
    """
    Clase responsable de la ingeniería de características para el modelo.
    
    Maneja la creación de nuevas features, codificación de categóricas,
    escalado de numéricas y partición de datos, respetando la prevención
    de fuga de información.
    """
    
    def __init__(self, target_column: str = 'early_default'):
        """
        Inicializa el FeatureEngineer.
        
        Args:
            target_column: Nombre de la variable objetivo.
        """
        self.target_column = target_column
        self.feature_names: List[str] = []
        self.categorical_cols: List[str] = []
        self.numerical_cols: List[str] = []
        self.label_encoders: Dict[str, LabelEncoder] = {}
        self.onehot_encoder: Optional[OneHotEncoder] = None
        self.scaler: Optional[StandardScaler] = None
        self.preprocessor: Optional[ColumnTransformer] = None
        
    def identify_column_types(self, df: pd.DataFrame) -> None:
        """
        Identifica automáticamente los tipos de columnas.
        
        Args:
            df: DataFrame de entrada.
        """
        self.numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if self.target_column in self.numerical_cols:
            self.numerical_cols.remove(self.target_column)
        if 'loan_id' in self.numerical_cols:
            self.numerical_cols.remove('loan_id')
            
        self.categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
        
        logger.info(f"Columnas numéricas ({len(self.numerical_cols)}): {self.numerical_cols}")
        logger.info(f"Columnas categóricas ({len(self.categorical_cols)}): {self.categorical_cols}")
    
    def create_domain_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Crea features basadas en conocimiento del dominio.
        
        Args:
            df: DataFrame de entrada.
            
        Returns:
            DataFrame con nuevas features creadas.
        """
        logger.info("Creando features de dominio...")
        df_new = df.copy()
        
        # Ratio de préstamo respecto al ingreso
        if 'loan_amount' in df_new.columns and 'income' in df_new.columns:
            df_new['loan_to_income_ratio'] = df_new['loan_amount'] / (df_new['income'] + 1)
            logger.debug("Creada feature: loan_to_income_ratio")
        
        # Cuota mensual estimada
        if 'loan_amount' in df_new.columns and 'loan_term' in df_new.columns:
            df_new['monthly_payment_estimate'] = df_new['loan_amount'] / (df_new['loan_term'] + 1)
            logger.debug("Creada feature: monthly_payment_estimate")
        
        # Ratio de cuota mensual respecto al ingreso
        if 'monthly_payment_estimate' in df_new.columns and 'income' in df_new.columns:
            df_new['payment_to_income_ratio'] = df_new['monthly_payment_estimate'] / (df_new['income'] + 1)
            logger.debug("Creada feature: payment_to_income_ratio")
        
        # Score normalizado
        if 'credit_score' in df_new.columns:
            df_new['credit_score_normalized'] = (df_new['credit_score'] - 300) / (850 - 300)
            logger.debug("Creada feature: credit_score_normalized")
        
        # Categoría de edad
        if 'age' in df_new.columns:
            df_new['age_group'] = pd.cut(
                df_new['age'],
                bins=[0, 25, 35, 45, 55, 100],
                labels=['18-25', '26-35', '36-45', '46-55', '55+']
            )
            df_new['age_group'] = df_new['age_group'].astype(str)
            logger.debug("Creada feature: age_group")
        
        # Estabilidad laboral (empleos / años)
        if 'employment_years' in df_new.columns and 'existing_loans' in df_new.columns:
            df_new['employment_stability'] = df_new['employment_years'] / (df_new['existing_loans'] + 1)
            logger.debug("Creada feature: employment_stability")
        
        # Interacción income * credit_score
        if 'income' in df_new.columns and 'credit_score' in df_new.columns:
            df_new['income_credit_interaction'] = df_new['income'] * df_new['credit_score'] / 10000
            logger.debug("Creada feature: income_credit_interaction")
        
        # Riesgo deuda
        if 'debt_to_income' in df_new.columns and 'existing_loans' in df_new.columns:
            df_new['debt_risk_score'] = df_new['debt_to_income'] * (df_new['existing_loans'] + 1)
            logger.debug("Creada feature: debt_risk_score")
        
        logger.info(f"Features de dominio creadas. Shape: {df_new.shape}")
        return df_new
    
    def encode_categorical(self, df: pd.DataFrame, method: str = 'onehot') -> pd.DataFrame:
        """
        Codifica variables categóricas.
        
        Args:
            df: DataFrame de entrada.
            method: 'onehot' o 'label'
            
        Returns:
            DataFrame con categóricas codificadas.
        """
        logger.info(f"Codificando categóricas con método: {method}")
        df_encoded = df.copy()
        
        if method == 'label':
            for col in self.categorical_cols:
                if col in df_encoded.columns:
                    le = LabelEncoder()
                    df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
                    self.label_encoders[col] = le
                    logger.debug(f"Label encoded: {col}")
                    
        elif method == 'onehot':
            df_encoded = pd.get_dummies(df_encoded, columns=self.categorical_cols, drop_first=True)
            logger.debug(f"One-hot encoded: {self.categorical_cols}")
            
        self.feature_names = [c for c in df_encoded.columns if c != self.target_column]
        logger.info(f"Total features después de codificación: {len(self.feature_names)}")
        return df_encoded
    
    def build_preprocessor(self, df: pd.DataFrame) -> ColumnTransformer:
        """
        Construye un preprocesador sklearn para transformations reproducibles.
        
        Args:
            df: DataFrame de referencia.
            
        Returns:
            ColumnTransformer configurado.
        """
        self.identify_column_types(df)
        
        # Actualizar listas después de crear features de dominio
        numerical_features = [c for c in df.columns if c in self.numerical_cols or 
                            (df[c].dtype in [np.number] and c != self.target_column and c != 'loan_id')]
        categorical_features = [c for c in df.columns if c in self.categorical_cols]
        
        if 'age_group' in df.columns:
            categorical_features.append('age_group')
        
        numerical_features = [c for c in numerical_features if c not in categorical_features]
        
        logger.info(f"Building preprocessor - Numéricas: {len(numerical_features)}, Categóricas: {len(categorical_features)}")
        
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_features),
                ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), categorical_features)
            ],
            remainder='drop'
        )
        
        return self.preprocessor
    
    def split_data(
        self, 
        df: pd.DataFrame, 
        test_size: float = 0.2, 
        val_size: float = 0.1,
        random_state: int = 42,
        stratify: bool = True
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, pd.Series]:
        """
        Parte los datos en train/validation/test.
        
        CRÍTICO: La partición se hace ANTES de cualquier transformación para evitar
        data leakage. El preprocessor se ajusta solo con datos de entrenamiento.
        
        Args:
            df: DataFrame completo.
            test_size: Proporción para test.
            val_size: Proporción para validación (del train).
            random_state: Semilla para reproducibilidad.
            stratify: Si True, mantiene proporción de clases.
            
        Returns:
            Tupla (X_train, X_val, X_test, y_train, y_val, y_test).
        """
        logger.info(f"Particionando datos (test={test_size}, val={val_size})")
        
        X = df.drop(columns=[self.target_column])
        y = df[self.target_column]
        
        stratify_param = y if stratify else None
        
        # Primera partición: train + test
        X_train_full, X_test, y_train_full, y_test = train_test_split(
            X, y, 
            test_size=test_size, 
            random_state=random_state, 
            stratify=stratify_param
        )
        
        # Segunda partición: train + validation
        val_adjusted_size = val_size / (1 - test_size)
        X_train, X_val, y_train, y_val = train_test_split(
            X_train_full, y_train_full,
            test_size=val_adjusted_size,
            random_state=random_state,
            stratify=stratify_param
        )
        
        logger.info(f"Train: {len(X_train)}, Validation: {len(X_val)}, Test: {len(X_test)}")
        logger.info(f"Distribución target - Train: {y_train.value_counts().to_dict()}")
        
        return X_train, X_val, X_test, y_train, y_val, y_test
    
    def fit_transform(
        self, 
        X_train: pd.DataFrame, 
        X_val: Optional[pd.DataFrame] = None,
        X_test: Optional[pd.DataFrame] = None
    ) -> Tuple[np.ndarray, ...]:
        """
        Ajusta el preprocesador con datos de entrenamiento y transforma todos los conjuntos.
        
        Args:
            X_train: Datos de entrenamiento.
            X_val: Datos de validación (opcional).
            X_test: Datos de prueba (opcional).
            
        Returns:
            Tupla de arrays transformados.
        """
        logger.info("Ajustando preprocesador y transformando datos...")
        
        # Construir preprocesador
        self.build_preprocessor(X_train)
        
        # Ajustar y transformar train
        X_train_transformed = self.preprocessor.fit_transform(X_train)
        
        # Transformar val y test con el mismo preprocesador
        results = [X_train_transformed]
        
        if X_val is not None:
            X_val_transformed = self.preprocessor.transform(X_val)
            results.append(X_val_transformed)
            
        if X_test is not None:
            X_test_transformed = self.preprocessor.transform(X_test)
            results.append(X_test_transformed)
        
        # Obtener nombres de features
        self.feature_names = self.preprocessor.get_feature_names_out()
        logger.info(f"Features transformadas: {len(self.feature_names)}")
        
        return tuple(results)
    
    def save_preprocessor(self, path: str) -> None:
        """
        Guarda el preprocesador para uso futuro.
        
        Args:
            path: Ruta donde guardar el preprocesador.
        """
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        joblib.dump({
            'preprocessor': self.preprocessor,
            'label_encoders': self.label_encoders,
            'feature_names': self.feature_names,
            'numerical_cols': self.numerical_cols,
            'categorical_cols': self.categorical_cols
        }, path)
        logger.info(f"Preprocesador guardado en: {path}")
    
    def load_preprocessor(self, path: str) -> None:
        """
        Carga un preprocesador previamente guardado.
        
        Args:
            path: Ruta del preprocesador guardado.
        """
        data = joblib.load(path)
        self.preprocessor = data['preprocessor']
        self.label_encoders = data['label_encoders']
        self.feature_names = data['feature_names']
        self.numerical_cols = data['numerical_cols']
        self.categorical_cols = data['categorical_cols']
        logger.info(f"Preprocesador cargado desde: {path}")


def build_features_pipeline(
    data_path: str,
    output_dir: str,
    test_size: float = 0.2,
    val_size: float = 0.1
) -> Dict[str, any]:
    """
    Función de alto nivel para ejecutar el pipeline completo de features.
    
    Args:
        data_path: Ruta al archivo de datos procesados.
        output_dir: Directorio para guardar resultados.
        test_size: Proporción de test.
        val_size: Proporción de validación.
        
    Returns:
        Diccionario con datasets y preprocesador.
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Cargar datos
    logger.info(f"Cargando datos desde: {data_path}")
    df = pd.read_csv(data_path)
    
    # Inicializar feature engineer
    engineer = FeatureEngineer(target_column='early_default')
    
    # Identificar tipos
    engineer.identify_column_types(df)
    
    # Crear features de dominio
    df = engineer.create_domain_features(df)
    
    # Particionar datos (ANTES de transformar para evitar leakage)
    X_train, X_val, X_test, y_train, y_val, y_test = engineer.split_data(
        df, test_size=test_size, val_size=val_size
    )
    
    # Ajustar preprocesador y transformar
    X_train_transformed, X_val_transformed, X_test_transformed = engineer.fit_transform(
        X_train, X_val, X_test
    )
    
    # Guardar preprocesador
    preprocessor_path = output_path / 'preprocessor.joblib'
    engineer.save_preprocessor(str(preprocessor_path))
    
    # Guardar datasets transformados
    np.save(output_path / 'X_train.npy', X_train_transformed)
    np.save(output_path / 'X_val.npy', X_val_transformed)
    np.save(output_path / 'X_test.npy', X_test_transformed)
    y_train.to_csv(output_path / 'y_train.csv', index=False)
    y_val.to_csv(output_path / 'y_val.csv', index=False)
    y_test.to_csv(output_path / 'y_test.csv', index=False)
    
    logger.info(f"Pipeline completado. Datos guardados en: {output_path}")
    
    return {
        'X_train': X_train_transformed,
        'X_val': X_val_transformed,
        'X_test': X_test_transformed,
        'y_train': y_train,
        'y_val': y_val,
        'y_test': y_test,
        'preprocessor': engineer.preprocessor,
        'feature_names': engineer.feature_names
    }


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else '../data/features'
    else:
        input_path = '../data/processed/loan_data_cleaned.csv'
        output_dir = '../data/features'
    
    results = build_features_pipeline(input_path, output_dir)
    print(f"\n=== PIPELINE COMPLETADO ===")
    print(f"X_train shape: {results['X_train'].shape}")
    print(f"X_val shape: {results['X_val'].shape}")
    print(f"X_test shape: {results['X_test'].shape}")
    print(f"Features: {len(results['feature_names'])}")