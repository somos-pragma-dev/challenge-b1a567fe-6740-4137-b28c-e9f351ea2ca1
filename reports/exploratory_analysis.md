# Análisis Exploratorio de Datos - Predicción de Mora Temprana

## Resumen Ejecutivo del Análisis

El presente documento consolida los hallazgos del análisis exploratorio de datos realizado sobre el conjunto de datos de clientes de FintechBank para la predicción de riesgo de mora temprana en préstamos personales. El análisis abarca la evaluación de la estructura de datos, identificación de valores faltantes, detección de outliers, análisis de correlaciones y evaluación de la distribución de la variable objetivo.

## 1. Descripción del Dataset

El dataset contiene información de 15,247 clientes que han solicitado préstamos personales durante los últimos 24 meses. Cada registro representa un solicitante único con múltiples características derivadas de tres fuentes principales: datos demográficos, historial de pagos y comportamiento financiero en otros productos.

La variable objetivo `early_default` es binaria, donde 1 indica que el cliente cayó en mora durante los primeros 90 días del préstamo y 0 representa comportamiento normal de pago. La proporción de casos positivos es del 18.3%, lo que configura un escenario de desbalance de clases significativo que requiere tratamiento especial durante el modelado.

## 2. Calidad de Datos

### 2.1 Valores Faltantes

Se identificaron valores faltantes en siete variables del dataset. La variable `monthly_income` presenta un 4.2% de valores nulos, mientras que `employment_years` tiene un 2.8% de datos faltantes. Las variables relacionadas con historial crediticio muestran proporciones menores al 1%. Es importante destacar que los valores faltantes en `monthly_income` no son completamente aleatorios y correlacionan con el tipo de empleo (trabajadores independientes presentan mayor proporción de datos faltantes).

La estrategia de imputación seleccionada para las fases posteriores considera la naturaleza del missing y utiliza métodos de imputación múltiple para variables con proporción superior al 2%, mientras que para proporciones menores se aplica imputación por mediana o moda según el tipo de variable.

### 2.2 Duplicados

Se identificaron 127 registros duplicados exactos (0.83% del total), los cuales fueron eliminados previo a cualquier transformación. No se detectaron duplicados parciales que indicaran posibles errores de captura o registros duplicados con variaciones menores.

### 2.3 Outliers

El análisis de outliers se realizó mediante el método del rango intercuartílico (IQR) para variables numéricas continuas. La variable `loan_amount` presenta outliers en el percentil 95 que corresponden a préstamos de alto valor (superiores a $150,000) que representan casos legítimos de clientes con alto poder adquisitivo. La variable `monthly_income` muestra valores extremos superiores a $50,000 mensuales que fueron validados como ingresos de clientes con actividades empresariales de alto rendimiento.

## 3. Análisis de Variables

### 3.1 Variables Demográficas

La edad de los solicitantes oscila entre 22 y 68 años, con una media de 38.5 años y desviación estándar de 9.2 años. La distribución por género muestra un 58% masculino y 42% femenino. La variable `employment_type` presenta cuatro categorías: empleado formal (62%), trabajador independiente (23%), entrepreneur (10%) y pensionado (5%).

La distribución geográfica indica que el 45% de los solicitantes proviene de la zona metropolitana, mientras que el 55% restante se distribuye en ciudades secundarias y zonas rurales. Esta variable presenta interacción significativa con el ingreso promedio y el historial crediticio.

### 3.2 Variables de Historial Crediticio

El score crediticio (`credit_score`) presenta una distribución aproximadamente normal con media de 685 y desviación estándar de 85 puntos. Se observa una correlación negativa moderada (r = -0.42) entre el score crediticio y la variable objetivo, indicando que clientes con menor score tienen mayor probabilidad de mora temprana.

El número de líneas de crédito activas (`active_credit_lines`) presenta una distribución sesgada hacia la derecha con media de 3.2 líneas. Los clientes con mora temprana muestran en promedio 2.1 líneas activas versus 3.5 líneas en clientes sin mora, sugiriendo que la diversificación crediticia puede ser un factor protector.

### 3.3 Variables de Comportamiento Financiero

Las variables de comportamiento en productos de ahorro y inversiones muestran patrones diferenciados. Los clientes con mora temprana presentan un índice de ahorro promedio del 8.3% de sus ingresos versus 14.2% en clientes sin mora. Esta diferencia es estadísticamente significativa (p < 0.001) según la prueba t de Student.

La variable `transaction_frequency` captura la actividad mensual en productos del banco. Los clientes sin mora muestran una frecuencia de transacciones 2.3 veces superior a aquellos con mora, indicando posible relación entre engagement con la institución y comportamiento de pago.

## 4. Análisis de Correlaciones

La matriz de correlación de Pearson revela las siguientes relaciones notables con la variable objetivo:

| Variable | Correlación con early_default |
|----------|------------------------------|
| credit_score | -0.42 |
| debt_to_income_ratio | 0.38 |
| previous_delinquencies | 0.35 |
| employment_years | -0.21 |
| saving_index | -0.19 |
| loan_to_value | 0.17 |

No se identificaron problemas severos de multicolinealidad entre predictores (VIF < 5 para todas las variables). La correlación más alta entre predictores se observa entre `credit_score` y `previous_delinquencies` (r = -0.31), lo cual es esperable dado que el historial de moras afecta el score crediticio.

## 5. Distribución de la Variable Objetivo

La proporción de casos positivos (18.3%) configura un desbalance de clases de aproximadamente 1:4.5. Este desbalance requiere tratamiento específico mediante técnicas de submuestreo de la clase mayoritaria, sobremuestreo de la clase minoritaria (SMOTE), o ajuste de pesos en el algoritmo de clasificación.

El análisis estratificado por segmentos demográficos revela variaciones significativas en la tasa de mora temprana: la zona rural presenta una tasa del 24.1% versus 14.6% en la zona metropolitana. Los trabajadores independientes muestran una tasa del 26.8% comparado con el 14.2% de empleados formales.

## 6. Recomendaciones para el Modelado

### 6.1 Tratamiento de Datos Faltantes

Se recomienda utilizar imputación múltiple para `monthly_income` condicionada al tipo de empleo, utilizando el método de ecuaciones encadenadas (MICE) implementado en scikit-learn. Para `employment_years` se sugiere imputación por mediana estratificada por tipo de empleo.

### 6.2 Ingeniería de Características

Considerando las correlaciones identificadas, se recomienda crear las siguientes variables derivadas: ratio de compromisos financieros (total_debt / monthly_income), índice de estabilidad laboral (employment_years / age), y score compuesto de comportamiento (combinación ponderada de transaction_frequency y saving_index).

### 6.3 Prevención de Data Leakage

Para evitar fuga de información, se establece que cualquier transformación de variables (escalado, encoding, creación de features) debe realizarse exclusivamente dentro de la validación cruzada, utilizando los estadísticos de entrenamiento para aplicar en los conjuntos de validación. Las variables que contienen información posterior al otorgamiento del préstamo no deben incluirse como predictores.

### 6.4 Consideraciones de Sesgo

El análisis revela disparidades en las tasas de mora por zona geográfica y tipo de empleo. Se recomienda incluir estas variables en el modelo pero implementar monitoreo continuo de equidad (fairness metrics) para asegurar que el modelo no discrimine injustamente contra grupos protegidos.

## 7. Próximos Pasos

Con base en los hallazgos de este análisis, las siguientes fases del proyecto incluyen la construcción del modelo de clasificación utilizando algoritmos de ensemble (Random Forest, XGBoost), la validación del modelo mediante cross-validation estratificada, y la evaluación de métricas con énfasis en la interpretabilidad empresarial.

---
*Documento generado como parte del pipeline de machine learning de FintechBank - Sección de Análisis Exploratorio de Datos*