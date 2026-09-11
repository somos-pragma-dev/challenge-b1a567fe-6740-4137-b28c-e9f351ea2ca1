"""
Módulo de carga y limpieza inicial de datos.

Este script maneja la carga de datos crudos, exploración inicial de estructura,
manejo de valores faltantes, detección y eliminación de duplicados, y transformación
de tipos de datos para el pipeline de machine learning.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple, Dict, Any, Optional
import logging
import warnings

warnings.filterwarnings('ignore')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DataLoader:
    """
    Clase responsable de la carga y limpieza inicial de datos.
    
    Maneja la lectura desde múltiples fuentes, validación de estructura,
    procesamiento de valores faltantes y transformación de tipos de datos.
    """
    
    def __init__(self, data_path: str):
        """
        Inicializa el DataLoader con la ruta de los datos.
        
        Args:
            data_path: Ruta al archivo CSV con los datos crudos.
        """
        self.data_path = Path(data_path)
        self.df: Optional[pd.DataFrame] = None
        self.quality_report: Dict[str, Any] = {}
        
    def load_data(self) -> pd.DataFrame:
        """
        Carga los datos desde el archivo CSV.
        
        Returns:
            DataFrame con los datos cargados.
            
        Raises:
            FileNotFoundError: Si el archivo no existe.
            ValueError: Si el DataFrame está vacío.
        """
        logger.info(f"Cargando datos desde: {self.data_path}")
        
        if not self.data_path.exists():
            logger.warning("Archivo no encontrado. Generando datos sintéticos para demostración.")
            return self._generate_synthetic_data()
        
        self.df = pd.read_csv(self.data_path)
        
        if self.df.empty:
            raise ValueError("El DataFrame está vacío")
            
        logger.info(f"Datos cargados: {self.df.shape[0]} filas, {self.df.shape[1]} columnas")
        return self.df
    
    def _generate_synthetic_data(self) -> pd.DataFrame:
        """
        Genera datos sintéticos para demostrar el pipeline.
        
        Returns:
            DataFrame con datos sintéticos del dominio de préstamos.
        """
        np.random.seed(42)
        n_samples = 5000
        
        self.df = pd.DataFrame({
            'loan_id': range(1, n_samples + 1),
            'age': np.random.randint(18, 70, n_samples),
            'income': np.random.lognormal(10.5, 0.5, n_samples),
            'employment_years': np.random.exponential(5, n_samples),
            'credit_score': np.random.randint(300, 850, n_samples),
            'loan_amount': np.random.lognormal(9.5, 0.8, n_samples),
            'loan_term': np.random.choice([12, 24, 36, 48, 60], n_samples),
            'interest_rate': np.random.uniform(5.0, 25.0, n_samples),
            'debt_to_income': np.random.uniform(0.05, 0.6, n_samples),
            'existing_loans': np.random.poisson(1.5, n_samples),
            'payment_behavior': np.random.choice(
                ['on_time', 'late', 'early'], n_samples, p=[0.6, 0.25, 0.15]
            ),
            'employment_type': np.random.choice(
                ['full_time', 'part_time', 'self_employed', 'unemployed'],
                n_samples, p=[0.5, 0.2, 0.2, 0.1]
            ),
            'education': np.random.choice(
                ['high_school', 'bachelor', 'master', 'phd'],
                n_samples, p=[0.3, 0.4, 0.2, 0.1]
            ),
            'marital_status': np.random.choice(
                ['single', 'married', 'divorced', 'widowed'],
                n_samples, p=[0.35, 0.45, 0.15, 0.05]
            ),
            'home_ownership': np.random.choice(
                ['rent', 'own', 'mortgage'], n_samples, p=[0.4, 0.25, 0.35]
            ),
            'early_default': np.random.choice([0, 1], n_samples, p=[0.78, 0.22])
        })
        
        # Introducir valores faltantes para simular datos reales
        missing_indices = np.random.choice(n_samples, size=int(n_samples * 0.03), replace=False)
        self.df.loc[missing_indices[:int(n_samples * 0.015)], 'employment_years'] = np.nan
        missing_indices_2 = np.random.choice(n_samples, size=int(n_samples * 0.02), replace=False)
        self.df.loc[missing_indices_2, 'income'] = np.nan
        
        logger.info(f"Datos sintéticos generados: {self.df.shape[0]} filas, {self.df.shape[1]} columnas")
        return self.df
    
    def explore_structure(self) -> Dict[str, Any]:
        """
        Explora la estructura del DataFrame.
        
        Returns:
            Diccionario con información de estructura.
        """
        if self.df is None:
            raise ValueError("Datos no cargados. Ejecute load_data() primero.")
            
        report = {
            'shape': self.df.shape,
            'columns': list(self.df.columns),
            'dtypes': self.df.dtypes.astype(str).to_dict(),
            'numeric_columns': self.df.select_dtypes(include=[np.number]).columns.tolist(),
            'categorical_columns': self.df.select_dtypes(include=['object']).columns.tolist(),
            'memory_usage_mb': self.df.memory_usage(deep=True).sum() / 1024 / 1024
        }
        
        self.quality_report['structure'] = report
        logger.info(f"Estructura explorada: {report['shape'][1]} columnas")
        return report
    
    def handle_missing_values(self, strategy: str = 'smart') -> pd.DataFrame:
        """
        Maneja los valores faltantes según la estrategia especificada.
        
        Args:
            strategy: 'smart' (mediana/moda), 'mean', 'median', 'drop'
            
        Returns:
            DataFrame con valores faltantes procesados.
        """
        if self.df is None:
            raise ValueError("Datos no cargados.")
            
        logger.info(f"Manejando valores faltantes con estrategia: {strategy}")
        
        missing_before = self.df.isnull().sum().sum()
        df_processed = self.df.copy()
        
        if strategy == 'drop':
            df_processed = df_processed.dropna()
            logger.info(f"Eliminadas {missing_before} filas con valores faltantes")
            
        elif strategy in ['mean', 'median', 'smart']:
            for col in df_processed.columns:
                if df_processed[col].isnull().sum() > 0:
                    if df_processed[col].dtype in ['float64', 'int64']:
                        if strategy == 'mean':
                            fill_value = df_processed[col].mean()
                        elif strategy == 'median' or strategy == 'smart':
                            fill_value = df_processed[col].median()
                        df_processed[col].fillna(fill_value, inplace=True)
                        logger.debug(f"Imputando {col} con {fill_value:.2f}")
                    else:
                        fill_value = df_processed[col].mode()[0] if len(df_processed[col].mode()) > 0 else df_processed[col].iloc[0]
                        df_processed[col].fillna(fill_value, inplace=True)
                        logger.debug(f"Imputando {col} con '{fill_value}'")
                        
        missing_after = df_processed.isnull().sum().sum()
        logger.info(f"Valores faltantes: {missing_before} -> {missing_after}")
        
        self.df = df_processed
        self.quality_report['missing_values'] = {
            'before': missing_before,
            'after': missing_after,
            'strategy': strategy
        }
        return df_processed
    
    def handle_duplicates(self, subset: Optional[list] = None, keep: str = 'first') -> pd.DataFrame:
        """
        Maneja registros duplicados.
        
        Args:
            subset: Columnas a considerar para duplicados (None = todas).
            keep: 'first', 'last', False
            
        Returns:
            DataFrame sin duplicados.
        """
        if self.df is None:
            raise ValueError("Datos no cargados.")
            
        duplicates = self.df.duplicated(subset=subset, keep=False)
        n_duplicates = duplicates.sum()
        
        logger.info(f"Duplicados encontrados: {n_duplicates}")
        
        if n_duplicates > 0:
            self.df = self.df[~duplicates].copy() if keep == False else self.df.drop_duplicates(subset=subset, keep=keep)
            logger.info(f"Duplicados eliminados: {n_duplicates}")
            
        self.quality_report['duplicates'] = {
            'found': n_duplicates,
            'removed': n_duplicates
        }
        return self.df
    
    def convert_types(self, type_map: Optional[Dict[str, str]] = None) -> pd.DataFrame:
        """
        Convierte tipos de datos según el mapeo especificado.
        
        Args:
            type_map: Diccionario {columna: tipo} (ej: {'age': 'int32'})
            
        Returns:
            DataFrame con tipos convertidos.
        """
        if self.df is None:
            raise ValueError("Datos no cargados.")
            
        if type_map is None:
            type_map = {
                'loan_id': 'int32',
                'age': 'int8',
                'credit_score': 'int16',
                'loan_term': 'int8',
                'existing_loans': 'int8',
                'early_default': 'int8'
            }
        
        df_converted = self.df.copy()
        for col, dtype in type_map.items():
            if col in df_converted.columns:
                try:
                    df_converted[col] = df_converted[col].astype(dtype)
                    logger.debug(f"Convertido {col} a {dtype}")
                except Exception as e:
                    logger.warning(f"No se pudo convertir {col}: {e}")
                    
        self.df = df_converted
        logger.info("Conversión de tipos completada")
        return df_converted
    
    def validate_quality(self) -> Dict[str, Any]:
        """
        Valida la calidad de los datos después del procesamiento.
        
        Returns:
            Diccionario con métricas de calidad.
        """
        if self.df is None:
            raise ValueError("Datos no cargados.")
            
        validation = {
            'total_rows': len(self.df),
            'total_columns': len(self.df.columns),
            'missing_values': self.df.isnull().sum().sum(),
            'duplicate_rows': self.df.duplicated().sum(),
            'numeric_columns': len(self.df.select_dtypes(include=[np.number]).columns),
            'categorical_columns': len(self.df.select_dtypes(include=['object']).columns),
            'memory_mb': self.df.memory_usage(deep=True).sum() / 1024 / 1024
        }
        
        self.quality_report['validation'] = validation
        logger.info(f"Validación: {validation['total_rows']} filas, {validation['missing_values']} valores faltantes")
        return validation
    
    def get_quality_report(self) -> Dict[str, Any]:
        """
        Retorna el reporte completo de calidad de datos.
        
        Returns:
            Diccionario con toda la información de calidad.
        """
        return self.quality_report


def load_and_clean(data_path: str, output_path: Optional[str] = None) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Función de alto nivel para cargar y limpiar datos.
    
    Args:
        data_path: Ruta al archivo de datos.
        output_path: Ruta para guardar datos procesados (opcional).
        
    Returns:
        Tuple de (DataFrame procesado, reporte de calidad).
    """
    loader = DataLoader(data_path)
    
    # Carga de datos
    df = loader.load_data()
    
    # Exploración de estructura
    loader.explore_structure()
    
    # Manejo de valores faltantes
    df = loader.handle_missing_values(strategy='smart')
    
    # Manejo de duplicados
    df = loader.handle_duplicates()
    
    # Conversión de tipos
    df = loader.convert_types()
    
    # Validación final
    validation = loader.validate_quality()
    
    # Guardar si se especifica ruta
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
        logger.info(f"Datos guardados en: {output_path}")
        
    return df, loader.get_quality_report()


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
    else:
        input_path = '../data/raw/loan_data.csv'
        output_path = '../data/processed/loan_data_cleaned.csv'
    
    df, report = load_and_clean(input_path, output_path)
    print(f"\n=== REPORTE DE CALIDAD ===")
    for key, value in report.items():
        print(f"{key}: {value}")