import pytest
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    recall_score, precision_score, f1_score, accuracy_score,
    roc_auc_score, confusion_matrix, classification_report
)
from typing import Dict, Any


class TestModelMetrics:
    """Pruebas para validar que las métricas del modelo cumplen umbrales mínimos."""

    @pytest.fixture
    def trained_model_and_data(self) -> Dict[str, Any]:
        """Entrena un modelo básico y devuelve datos de prueba."""
        np.random.seed(42)
        n_samples = 500
        
        X = pd.DataFrame({
            'edad': np.random.randint(18, 70, n_samples),
            'ingreso_mensual': np.random.uniform(1000, 15000, n_samples),
            'monto_prestamo': np.random.uniform(5000, 80000, n_samples),
            'plazo_meses': np.random.choice([12, 24, 36, 48, 60], n_samples),
            'historial_credito': np.random.randint(0, 6, n_samples),
            'score_credito': np.random.uniform(300, 850, n_samples),
            'n_deudas': np.random.randint(0, 5, n_samples)
        })
        
        # Generar target con cierta correlación
        probability = (
            0.3 * (X['historial_credito'] < 2).astype(int) +
            0.3 * (X['score_credito'] < 500).astype(int) +
            0.2 * (X['n_deudas'] >= 3).astype(int) +
            0.2 * np.random.random(n_samples)
        )
        y = (probability > 0.5).astype(int)
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        model = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        
        return {
            'model': model,
            'X_train': X_train,
            'X_test': X_test,
            'y_train': y_train,
            'y_test': y_test,
            'y_pred': y_pred,
            'y_pred_proba': y_pred_proba
        }

    def test_recall_positive_class_minimum(self, trained_model_and_data: Dict[str, Any]) -> None:
        """Verifica que el recall para la clase positiva cumpla con el umbral mínimo de 0.85."""
        y_test = trained_model_and_data['y_test']
        y_pred = trained_model_and_data['y_pred']
        
        recall = recall_score(y_test, y_pred, pos_label=1)
        MIN_RECALL = 0.85
        
        assert recall >= MIN_RECALL, (
            f"Recall de clase positiva es {recall:.3f}, menor al umbral {MIN_RECALL}. "
            f"El modelo no detecta suficientemente los casos de mora."
        )

    def test_precision_above_threshold(self, trained_model_and_data: Dict[str, Any]) -> None:
        """Verifica que la precisión tenga un valor razonable."""
        y_test = trained_model_and_data['y_test']
        y_pred = trained_model_and_data['y_pred']
        
        precision = precision_score(y_test, y_pred, pos_label=1)
        MIN_PRECISION = 0.60
        
        assert precision >= MIN_PRECISION, (
            f"Precisión es {precision:.3f}, menor al umbral {MIN_PRECISION}. "
            f"Demasiados falsos positivos."
        )

    def test_f1_score_acceptable(self, trained_model_and_data: Dict[str, Any]) -> None:
        """Verifica que el F1-score tenga un valor aceptable."""
        y_test = trained_model_and_data['y_test']
        y_pred = trained_model_and_data['y_pred']
        
        f1 = f1_score(y_test, y_pred, pos_label=1)
        MIN_F1 = 0.70
        
        assert f1 >= MIN_F1, f"F1-score es {f1:.3f}, menor al umbral {MIN_F1}"

    def test_accuracy_reasonable(self, trained_model_and_data: Dict[str, Any]) -> None:
        """Verifica que la exactitud general sea razonable."""
        y_test = trained_model_and_data['y_test']
        y_pred = trained_model_and_data['y_pred']
        
        accuracy = accuracy_score(y_test, y_pred)
        MIN_ACCURACY = 0.70
        
        assert accuracy >= MIN_ACCURACY, f"Exactitud es {accuracy:.3f}, menor al umbral {MIN_ACCURACY}"

    def test_roc_auc_above_chance(self, trained_model_and_data: Dict[str, Any]) -> None:
        """Verifica que el AUC-ROC esté significativamente por encima de 0.5 (azar)."""
        y_test = trained_model_and_data['y_test']
        y_pred_proba = trained_model_and_data['y_pred_proba']
        
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        MIN_AUC = 0.75
        
        assert roc_auc >= MIN_AUC, (
            f"AUC-ROC es {roc_auc:.3f}, menor al umbral {MIN_AUC}. "
            f"El modelo no tiene poder discriminativo suficiente."
        )

    def test_confusion_matrix_balanced(self, trained_model_and_data: Dict[str, Any]) -> None:
        """Verifica que la matriz de confusión tenga una distribución razonable."""
        y_test = trained_model_and_data['y_test']
        y_pred = trained_model_and_data['y_pred']
        
        cm = confusion_matrix(y_test, y_pred)
        tn, fp, fn, tp = cm.ravel()
        
        # Verificar que no haya un componente dominando completamente
        total = tn + fp + fn + tp
        
        assert tp > 0, "No hay verdaderos positivos detectados"
        assert tn > 0, "No hay verdaderos negativos detectados"
        
        # Verificar que la tasa de falsos negativos no sea excesivamente alta
        fnr = fn / (fn + tp) if (fn + tp) > 0 else 0
        assert fnr < 0.30, f"Tasa de falsos negativos muy alta: {fnr:.3f}"

    def test_classification_report_complete(self, trained_model_and_data: Dict[str, Any]) -> None:
        """Verifica que el reporte de clasificación contenga todas las métricas esperadas."""
        y_test = trained_model_and_data['y_test']
        y_pred = trained_model_and_data['y_pred']
        
        report = classification_report(y_test, y_pred, output_dict=True)
        
        assert '0' in report, "Falta información de la clase 0"
        assert '1' in report, "Falta información de la clase 1"
        assert 'macro avg' in report, "Faltan métricas macro promediadas"
        assert 'weighted avg' in report, "Faltan métricas ponderadas"
        
        # Verificar que ambas clases tengan métricas calculadas
        assert 'precision' in report['0'], "Falta precisión para clase 0"
        assert 'recall' in report['1'], "Falta recall para clase 1"
        assert 'f1-score' in report['macro avg'], "Falta F1-score en promedio"

    def test_business_cost_analysis(self, trained_model_and_data: Dict[str, Any]) -> None:
        """Analiza el costo business de los errores del modelo."""
        y_test = trained_model_and_data['y_test']
        y_pred = trained_model_and_data['y_pred']
        
        cm = confusion_matrix(y_test, y_pred)
        tn, fp, fn, tp = cm.ravel()
        
        # Costo estimado: falso negativo (mora no detectada) es más costoso
        COST_FN = 10000  # Pérdida por mora no detectada
        COST_FP = 1000   # Costo por rechazar buen cliente
        
        total_cost = (fn * COST_FN) + (fp * COST_FP)
        
        # El costo total no debe exceder un umbral razonable
        max_acceptable_cost = len(y_test) * 2000
        
        assert total_cost < max_acceptable_cost, (
            f"Costo total de errores: ${total_cost:,.0f} exceeds threshold ${max_acceptable_cost:,.0f}"
        )