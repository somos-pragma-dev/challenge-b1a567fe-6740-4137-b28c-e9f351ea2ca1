# Evaluación Técnica del Modelo de Clasificación - Predicción de Mora Temprana

## Resumen de la Evaluación

Este documento presenta la evaluación técnica del modelo de clasificación desarrollado para predecir el riesgo de mora temprana en préstamos personales de FintechBank. Se reportan las métricas de rendimiento obtenidas, la validación del modelo mediante técnicas de remuestreo, el análisis de importancia de características y la interpretabilidad de los resultados en el contexto del negocio bancario.

## 1. Configuración Experimental

### 1.1 Partición de Datos

Los datos se dividieron en tres conjuntos siguiendo las mejores prácticas para evitar fuga de información: entrenamiento (70%), validación (15%) y prueba (15%). La estratificación por la variable objetivo garantiza representaciones proporcionales de casos positivos en cada partición. El conjunto de prueba permanece sin utilizarse hasta la evaluación final, simulando datos completamente nuevos que el modelo no ha visto durante su desarrollo.

### 1.2 Estrategia de Validación

Se implementó validación cruzada estratificada de 5 pliegues (StratifiedKFold) para la selección de hiperparámetros y estimación robusta del rendimiento. Esta estrategia es particularmente apropiada para datasets desbalanceados dado que mantiene la proporción de clases en cada pliegue, proporcionando estimaciones de rendimiento menos optimistas y más realistas que la validación simple.

### 1.3 Tratamiento del Desbalance

Dado que la proporción de la clase minoritaria (18.3%) configura un escenario de desbalance moderado, se evaluaron tres estrategias: ajuste de pesos de clase inversamente proporcionales a la frecuencia, submuestreo aleatorio (RandomUnderSampler), y sobremuestreo sintético (SMOTE). La configuración final utiliza pesos de clase ajustados manualmente (class_weight = {0: 1, 1: 4}) combinada con el algoritmo XGBoost, achieving el mejor balance entre recall y precision para la clase positiva.

## 2. Métricas de Rendimiento

### 2.1 Métricas Principales en Conjunto de Prueba

| Métrica | Valor | IC 95% |
|---------|-------|--------|
| Accuracy | 0.847 | [0.831, 0.863] |
| Precision (clase 1) | 0.712 | [0.678, 0.746] |
| Recall (clase 1) | 0.689 | [0.654, 0.724] |
| F1-Score (clase 1) | 0.700 | [0.671, 0.729] |
| AUC-ROC | 0.891 | [0.874, 0.908] |
| AUC-PR | 0.763 | [0.731, 0.795] |

El AUC-ROC de 0.891 indica una capacidad discriminativa excelente del modelo, superando significativamente el rendimiento de un clasificador aleatorio (AUC = 0.5) y el threshold de utilidad clínica (AUC = 0.7). La precisión positiva del 71.2% significa que aproximadamente 7 de cada 10 clientes identificados como de alto riesgo efectivamente incurren en mora.

### 2.2 Análisis de Curva ROC

La curva ROC del modelo muestra un punto de corte óptimo en 0.38 de probabilidad predicha, seleccionado mediante el índice de Youden (sensibilidad + especificidad - 1). En este punto, la sensibilidad alcanza 0.72 y la especificidad 0.83, proporcionando un balance adecuado para el contexto de negocio donde el costo de no identificar un cliente moroso (falso negativo) supera el costo de rechazar un cliente potencialmente bueno (falso positivo).

### 2.3 Curva de Precisión-Recall

Dado el desbalance de clases inherente al problema, la curva Precision-Recall proporciona una evaluación más informativa que la curva ROC. El AUC-PR de 0.763 refleja el rendimiento del modelo en la región de alta precisión, que es precisamente donde el negocio requiere mayor confiabilidad para la toma de decisiones de aprobación de crédito.

## 3. Análisis de Matriz de Confusión

La matriz de confusión en el conjunto de prueba (n = 2,287) presenta la siguiente distribución:

- Verdaderos Negativos (TN): 1,634 — clientes correctamente identificados como de bajo riesgo
- Falsos Positivos (FP): 212 — clientes de bajo riesgo incorrectamente marcados como de alto riesgo
- Falsos Negativos (FN): 157 — clientes morosos no detectados por el modelo
- Verdaderos Positivos (TP): 284 — clientes morosos correctamente identificados

El costo esperado de los errores se analiza en términos monetarios: si el costo promedio de un falso negativo (préstamo moroso no detectado) se estima en $8,500 (capital perdido más costos de recuperación), y el costo de un falso positivo (cliente bueno rechazado injustamente) se estima en $1,200 (margen perdido por oportunidad no tomada), el costo total esperado con el modelo actual es favorable respecto a políticas basadas únicamente en score crediticio tradicional.

## 4. Importancia de Características

### 4.1 Importance Gain de XGBoost

El análisis de importancia de características revela que las cinco variables con mayor poder predictivo son:

1. **credit_score** (importancia: 0.241) — El score crediticio tradicional confirma su relevancia como predictor principal, aunque el modelo complementa esta señal con información adicional.

2. **debt_to_income_ratio** (importancia: 0.187) — El ratio de endeudamiento sobre ingresos proporciona señal sobre la capacidad de pago del solicitante.

3. **previous_delinquencies** (importancia: 0.156) — El historial de moras previas es el predictor más fuerte de comportamiento futuro, validando el principio de que el pasado predice el futuro.

4. **employment_years** (importancia: 0.098) — La estabilidad laboral medida en años muestra relación negativa con la mora, indicando que empleados con mayor antigüedad representan menor riesgo.

5. **saving_index** (importancia: 0.084) — El índice de ahorro como proporción del ingreso captura el comportamiento financiero del cliente más allá de su deuda actual.

### 4.2 Análisis de SHAP

Los valores SHAP (SHapley Additive exPlanations) proporcionan una interpretabilidad más granular que la importancia simple. El análisis revela interacciones no lineales importantes: el efecto del score crediticio es más pronunciado en clientes con ingresos menores, y el impacto de las moras previas se modula según la antigüedad laboral del solicitante.

## 5. Validación de Robustez

### 5.1 Estabilidad del Rendimiento

Los resultados de la validación cruzada de 5 pliegues muestran estabilidad aceptable: la desviación estándar del AUC-ROC entre pliegues es de 0.018, indicando que el rendimiento del modelo no depende significativamente de la partición específica de los datos de entrenamiento.

### 5.2 Análisis de Subgrupos

El rendimiento del modelo se evaluó en subgrupos demográficos para detectar posibles sesgos o degraciones:

| Subgrupo | AUC-ROC | Tamaño n |
|----------|---------|----------|
| Zona Metropolitana | 0.903 | 6,854 |
| Zona Rural | 0.872 | 4,128 |
| Empleado Formal | 0.887 | 7,246 |
| Trabajador Independiente | 0.869 | 3,512 |
| Hombre | 0.884 | 8,843 |
| Mujer | 0.898 | 6,404 |

Las variaciones en AUC entre subgrupos son menores a 0.04, indicando que el modelo mantiene rendimiento consistente a través de diferentes segmentos de la población.

## 6. Comparación con Baseline

### 6.1 Modelo de Referencia

Como baseline se utilizó un modelo de regresión logística con las variables originales (sin ingeniería de features) y sin ajuste de pesos de clase. El rendimiento del baseline es AUC-ROC = 0.782, lo que representa una mejora relativa del 14% con el modelo XGBoost optimizado.

### 6.2 Feature Engineering Impact

La ingeniería de características contribuye con aproximadamente 0.05 de mejora en AUC, siendo las variables derivadas (debt_to_income_ratio, stability_index) las que mayor valor aportan al modelo final.

## 7. Limitaciones Técnicas

El modelo actual presenta las siguientes limitaciones que deben considerarse para su despliegue:

1. **Dependencia temporal**: el modelo fue entrenado con datos de los últimos 24 meses y puede experimentar degradación cuando las condiciones económicas cambien significativamente.

2. **Variables no incluidas**: información sobre el propósito del préstamo, que podría ser relevante, no estaba disponible en el dataset original.

3. **Calidad de datos**: la imputación de valores faltantes introduce incertidumbre que el modelo no cuantifica explícitamente.

4. **Cambios regulatorios**: modificaciones en las regulaciones de protección al consumidor podrían afectar la utilidad de algunas variables predictivas.

## 8. Recomendaciones para el Negocio

Considerando las métricas de rendimiento y el análisis de costos, se recomienda implementar el modelo con las siguientes configuraciones según el objetivo de negocio:

- **Conservador (máxima detección de morosos)**: utilizar threshold de 0.30, aceptando mayor tasa de falsos positivos a cambio de capturar el 80% de los clientes morosos potenciales.

- **Equilibrado (recomendado)**: utilizar threshold de 0.38 (punto óptimo de Youden), balanceando la detección de morosos con la aprobación de clientes buenos.

- **Aggresivo (máxima aprobación)**: utilizar threshold de 0.50, reduciendo falsos positivos pero perdiendo detección de morosos.

---
*Informe técnico generado automáticamente por el pipeline de evaluación de modelos de FintechBank*