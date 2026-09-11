"""
Módulo de predicción para el modelo de riesgo de mora temprana.
Expone funcionalidad de inferencia sobre nuevos datos de solicitantes.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, Any, Optional, List
import joblib
import json
from datetime import datetime


class PredictionError(Exception):
    """Error específico para fallos en el pipeline de predicción."""
    pass


class ModelLoader:
    """Carga y valida los artefactos del modelo entrenado."""

    def __init__(self, model_path: str = "models/gradient_boosting_model.pkl"):
        self.model_path = Path(model_path)
        self._model = None
        self._feature_names = None
        self._categorical_columns = None
        self._numerical_columns = None

    def load(self) -> 'ModelLoader':
        """Carga el modelo y sus metadatos desde disco."""
        if not self.model_path.exists():
            raise PredictionError(f"Modelo no encontrado en: {self.model_path}")

        try:
            artifacts = joblib.load(self.model_path)
            self._model = artifacts.get('model')
            self._feature_names = artifacts.get('feature_names', [])
            self._categorical_columns = artifacts.get('categorical_columns', [])
            self._numerical_columns = artifacts.get('numerical_columns', [])

            if self._model is None:
                raise PredictionError("El archivo no contiene un modelo válido")

        except Exception as e:
            raise PredictionError(f"Error al cargar el modelo: {str(e)}")

        return self

    @property
    def model(self):
        return self._model

    @property
    def feature_names(self) -> List[str]:
        return self._feature_names

    @property
    def categorical_columns(self) -> List[str]:
        return self._categorical_columns

    @property
    def numerical_columns(self) -> List[str]:
        return self._numerical_columns


class DataValidator:
    """Valida los datos de entrada antes de la inferencia."""

    def __init__(self, feature_names: List[str], categorical_columns: List[str]):
        self.feature_names = feature_names
        self.categorical_columns = categorical_columns

    def validate(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Valida que los datos de entrada tengan las columnas requeridas.
        Retorna DataFrame limpio listo para inferencia.
        """
        missing_cols = set(self.feature_names) - set(data.columns)
        if missing_cols:
            raise PredictionError(
                f"Faltan columnas requeridas: {missing_cols}"
            )

        extra_cols = set(data.columns) - set(self.feature_names)
        if extra_cols:
            data = data.drop(columns=list(extra_cols))

        data = data[self.feature_names]

        for col in self.categorical_columns:
            if col in data.columns:
                data[col] = data[col].astype(str).fillna('desconocido')

        for col in data.columns:
            if col not in self.categorical_columns:
                if data[col].dtype == 'object':
                    data[col] = pd.to_numeric(data[col], errors='coerce')
                data[col] = data[col].fillna(data[col].median())

        return data


class RiskPredictor:
    """
    Orquestador principal para la predicción de riesgo de mora.
    Coordina carga del modelo, validación y generación de predicciones.
    """

    def __init__(self, model_path: str = "models/gradient_boosting_model.pkl"):
        self.loader = ModelLoader(model_path)
        self.loader.load()
        self.validator = DataValidator(
            self.loader.feature_names,
            self.loader.categorical_columns
        )

    def predict(self, data: pd.DataFrame) -> Dict[str, Any]:
        """
        Genera predicciones de riesgo para nuevos solicitantes.

        Args:
            data: DataFrame con los datos del solicitante.

        Returns:
            Diccionario con predicciones y metadatos.
        """
        try:
            validated_data = self.validator.validate(data)

            prediction = self.loader.model.predict(validated_data)
            probability = self.loader.model.predict_proba(validated_data)

            results = []
            for i in range(len(prediction)):
                results.append({
                    'prediction': int(prediction[i]),
                    'probability_no_mora': float(probability[i][0]),
                    'probability_mora': float(probability[i][1]),
                    'risk_level': self._classify_risk(probability[i][1])
                })

            return {
                'status': 'success',
                'timestamp': datetime.now().isoformat(),
                'predictions': results,
                'model_version': '1.0.0'
            }

        except PredictionError as e:
            return {
                'status': 'error',
                'error_type': 'ValidationError',
                'message': str(e),
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            return {
                'status': 'error',
                'error_type': 'PredictionError',
                'message': f"Error inesperado en predicción: {str(e)}",
                'timestamp': datetime.now().isoformat()
            }

    def predict_single(self, applicant_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Predicción para un único solicitante.

        Args:
            applicant_data: Diccionario con los datos del solicitante.

        Returns:
            Diccionario con la predicción individual.
        """
        data = pd.DataFrame([applicant_data])
        result = self.predict(data)

        if result['status'] == 'success':
            return result['predictions'][0]
        return result

    @staticmethod
    def _classify_risk(probability: float) -> str:
        """Clasifica el nivel de riesgo según la probabilidad."""
        if probability < 0.15:
            return 'bajo'
        elif probability < 0.40:
            return 'medio'
        elif probability < 0.70:
            return 'alto'
        else:
            return 'muy_alto'


def main():
    """
    Interfaz de línea de comandos para predicciones.
    Uso: python -m src.serve.predict --input data.csv --output predictions.json
    """
    import argparse

    parser = argparse.ArgumentParser(
        description='Predicción de riesgo de mora temprana'
    )
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Ruta al archivo CSV con datos de solicitantes'
    )
    parser.add_argument(
        '--output', '-o',
        default='predictions.json',
        help='Ruta para guardar las predicciones'
    )
    parser.add_argument(
        '--model', '-m',
        default='models/gradient_boosting_model.pkl',
        help='Ruta al modelo entrenado'
    )

    args = parser.parse_args()

    try:
        input_path = Path(args.input)
        if not input_path.exists():
            print(f"Error: Archivo de entrada no encontrado: {input_path}")
            return 1

        data = pd.read_csv(input_path)
        print(f"Cargados {len(data)} registros desde {input_path}")

        predictor = RiskPredictor(model_path=args.model)
        results = predictor.predict(data)

        output_path = Path(args.output)
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2, default=str)

        print(f"Predicciones guardadas en {output_path}")

        if results['status'] == 'success':
            predictions = results['predictions']
            mora_count = sum(1 for p in predictions if p['prediction'] == 1)
            print(f"Resumen: {mora_count}/{len(predictions)} casos de riesgo detectado")

        return 0

    except Exception as e:
        print(f"Error fatal: {str(e)}")
        return 1


if __name__ == '__main__':
    exit(main())


import pytest
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Any


class TestDataQuality:
    """Pruebas para validar la calidad de los datos procesados."""

    @pytest.fixture
    def sample_data(self) -> pd.DataFrame:
        """DataFrame de ejemplo para pruebas de calidad."""
        np.random.seed(42)
        n_samples = 100
        data = {
            'edad': np.random.randint(18, 70, n_samples),
            'ingreso_mensual': np.random.uniform(1000, 10000, n_samples),
            'monto_prestamo': np.random.uniform(5000, 50000, n_samples),
            'plazo_meses': np.random.choice([12, 24, 36, 48], n_samples),
            'historial_credito': np.random.choice([0, 1, 2, 3, 4, 5], n_samples),
            'estado_civil': np.random.choice(['soltero', 'casado', 'divorciado'], n_samples),
            'nivel_educativo': np.random.choice(['primaria', 'secundaria', 'universidad'], n_samples),
            'tipo_empleo': np.random.choice(['empleado', 'independiente', 'empresario'], n_samples),
            'tiene_deuda_activa': np.random.choice([0, 1], n_samples),
            'target': np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
        }
        df = pd.DataFrame(data)
        return df

    @pytest.fixture
    def data_with_missing(self) -> pd.DataFrame:
        """DataFrame con valores faltantes intencionales."""
        df = pd.DataFrame({
            'edad': [25, 30, np.nan, 45, 50],
            'ingreso_mensual': [2000, np.nan, 3000, 4500, 5000],
            'monto_prestamo': [10000, 15000, 20000, np.nan, 30000],
            'target': [0, 1, 0, 1, 0]
        })
        return df

    @pytest.fixture
    def data_with_duplicates(self) -> pd.DataFrame:
        """DataFrame con filas duplicadas."""
        df = pd.DataFrame({
            'edad': [25, 30, 25, 30, 35],
            'ingreso_mensual': [2000, 3000, 2000, 3000, 4000],
            'target': [0, 1, 0, 1, 0]
        })
        return df

    def test_no_missing_values_in_required_columns(self, sample_data: pd.DataFrame) -> None:
        """Verifica que las columnas requeridas no contengan valores faltantes."""
        required_columns = ['edad', 'ingreso_mensual', 'monto_prestamo', 'target']
        missing_counts = sample_data[required_columns].isnull().sum()
        
        for col in required_columns:
            assert missing_counts[col] == 0, f"Columna {col} tiene {missing_counts[col]} valores faltantes"

    def test_no_missing_values_in_categorical(self, sample_data: pd.DataFrame) -> None:
        """Verifica que columnas categóricas no tengan valores nulos."""
        categorical_columns = ['estado_civil', 'nivel_educativo', 'tipo_empleo']
        missing_in_categorical = sample_data[categorical_columns].isnull().sum()
        
        assert missing_in_categorical.sum() == 0, "Existen valores faltantes en columnas categóricas"

    def test_no_duplicate_rows(self, sample_data: pd.DataFrame) -> None:
        """Verifica que no existan filas duplicadas en el dataset."""
        duplicates = sample_data.duplicated().sum()
        assert duplicates == 0, f"Se encontraron {duplicates} filas duplicadas"

    def test_data_types_are_correct(self, sample_data: pd.DataFrame) -> None:
        """Verifica que los tipos de datos sean los esperados."""
        expected_types = {
            'edad': 'int64',
            'ingreso_mensual': 'float64',
            'monto_prestamo': 'float64',
            'plazo_meses': 'int64',
            'historial_credito': 'int64',
            'target': 'int64'
        }
        
        for col, expected_type in expected_types.items():
            actual_type = str(sample_data[col].dtype)
            assert actual_type == expected_type, f"Columna {col} tiene tipo {actual_type}, esperado {expected_type}"

    def test_target_variable_binary(self, sample_data: pd.DataFrame) -> None:
        """Verifica que la variable objetivo sea binaria (0 o 1)."""
        unique_values = sample_data['target'].unique()
        assert set(unique_values).issubset({0, 1}), f"Target contiene valores inválidos: {unique_values}"

    def test_numeric_columns_positive_ranges(self, sample_data: pd.DataFrame) -> None:
        """Verifica que las columnas numéricas estén en rangos positivos razonables."""
        assert (sample_data['edad'] > 0).all(), "Existen edades no positivas"
        assert (sample_data['ingreso_mensual'] > 0).all(), "Existen ingresos no positivos"
        assert (sample_data['monto_prestamo'] > 0).all(), "Existen montos de préstamo no positivos"

    def test_outlier_detection_basic(self, sample_data: pd.DataFrame) -> None:
        """Detecta valores atípicos extremos usando el método IQR."""
        numeric_cols = ['edad', 'ingreso_mensual', 'monto_prestamo']
        outlier_report: Dict[str, int] = {}
        
        for col in numeric_cols:
            Q1 = sample_data[col].quantile(0.25)
            Q3 = sample_data[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = ((sample_data[col] < lower_bound) | (sample_data[col] > upper_bound)).sum()
            outlier_report[col] = outliers
        
        for col, count in outlier_report.items():
            assert count < len(sample_data) * 0.05, f"Columna {col} tiene {count} outliers ({count/len(sample_data)*100:.1f}%)"

    def test_class_balance_reasonable(self, sample_data: pd.DataFrame) -> None:
        """Verifica que el balance de clases sea razonable para el entrenamiento."""
        class_counts = sample_data['target'].value_counts()
        min_class_ratio = class_counts.min() / class_counts.max()
        
        assert min_class_ratio > 0.1, f"Desequilibrio severo de clases: ratio mínimo = {min_class_ratio:.3f}"