# Resumen Ejecutivo - Modelo de Predicción de Mora Temprana

## Visión General del Proyecto

FintechBank ha desarrollado un modelo de machine learning para predecir el riesgo de mora temprana en préstamos personales, con el objetivo de mejorar las decisiones de aprobación de crédito y reducir las pérdidas financieras asociadas a defaults. El modelo alcanza un AUC-ROC de 0.891, indicando una capacidad discriminativa superior que permite identificar correctamente a clientes con alto riesgo de incumplimiento en el 72% de los casos, mientras mantiene una tasa de aprobación razonable para clientes de bajo riesgo.

## Resultados Principales

### Impacto Financiero Estimado

La implementación del modelo como herramienta de apoyo a la decisión de crédito genera los siguientes impactos proyectados sobre la cartera actual de préstamos:

**Reducción de pérdidas por mora**: el modelo permite identificar preventivamente al 72% de los clientes que eventualmente caerán en mora durante los primeros 90 días. Considerando una cartera activa de $45 millones y una tasa histórica de mora temprana del 18.3%, la prevención de aprobaciones de alto riesgo representa un ahorro potencial de $3.2 millones anuales en pérdidas evitadas.

**Optimización del proceso de aprobación**: la puntuación automatizada reduce el tiempo de evaluación de solicitudes de 48 horas a aproximadamente 3 segundos, permitiendo escalar el volumen de solicitudes sin incrementar el equipo de análisis crediticio. Esta eficiencia operativa representa un ahorro de $180,000 anuales en costos de personal.

**Mejora en la cobranza preventiva**: los clientes identificados como de alto riesgo pueden ser objeto de estrategias proactivas de cobranza antes de que incurran en mora, mejorando las tasas de recuperación y preservando la relación con el cliente.

### Métricas Clave del Modelo

| Indicador | Valor | Interpretación |
|-----------|-------|----------------|
| AUC-ROC | 0.891 | Excelente capacidad discriminativa |
| Precisión positiva | 71.2% | De cada 10 alertas de alto riesgo, 7 son correctas |
| Recall positivo | 68.9% | El modelo detecta casi 7 de cada 10 morosos potenciales |
| Especificidad | 83.4% | Alta tasa de aprobación correcta para clientes buenos |
| F1-Score | 0.700 | Balance adecuado entre precisión y recall |

## Sesgos y Limitaciones Identificadas

### Disparidades por Segmento Geográfico

El análisis de equidad del modelo revela diferencias en el rendimiento según la ubicación geográfica del solicitante. En zonas rurales, el modelo presenta una tasa de falsos positivos 4.3 puntos porcentuales superior que en zonas metropolitanas. Esta Disparidad se atribuye a la menor disponibilidad de información de comportamiento financiero en estas zonas, lo que fuerza al modelo a depender más heavily de variables proxy como el historial crediticio tradicional.

**Mitigación recomendada**: implementar un protocolo de revisión manual para solicitudes provenientes de zonas rurales que el modelo marque como alto riesgo, asegurando que la decisión final considere el contexto local.

### Limitaciones por Tipo de Empleo

Los trabajadores independientes presentan una tasa de detección de riesgo inferior (AUC = 0.869) comparado con empleados formales (AUC = 0.887). Esta diferencia se debe a la mayor variabilidad en los ingresos de este segmento y la menor disponibilidad de historial de nómina que sirva como señal de estabilidad.

**Mitigación recomendada**: solicitar documentación adicional de ingresos para este segmento y considerar la inclusión de variables alternativas como historial de transacciones bancarias y comportamiento de ahorro.

### Consideraciones de Equidad de Género

El análisis no revela sesgos significativos por género (AUC hombres: 0.884, AUC mujeres: 0.898), aunque las mujeres presentan una tasa ligeramente inferior de falsos positivos. El modelo se considera equitativo respecto a esta dimensión protegida.

## Recomendaciones Estratégicas

### Implementación Gradual

Se recomienda una implementación en tres fases para minimizar riesgos operativos:

**Fase 1 (meses 1-3)**: integrar el modelo como herramienta de información para los analistas de crédito, quienes mantienen la decisión final. Esta fase permite validar el rendimiento en producción y ajustar los thresholds según retroalimentación del equipo.

**Fase 2 (meses 4-6)**: implementar el modelo como sistema de recomendación con override manual disponible. Los analistas pueden aprobar o rechazar la recomendación del sistema documentando su justificación.

**Fase 3 (meses 7-12)**:迁移 hacia un sistema de decisión automatizada para segmentos de bajo riesgo (score > 0.7), manteniendo revisión humana para casos intermedios y alto riesgo.

### Monitoreo Continuo

El modelo requiere monitoreo continuo para detectar degradación de rendimiento. Se establecen los siguientes KPIs de monitoreo:

- AUC-ROC en ventana móvil de 30 días: alert si cae por debajo de 0.85
- Tasa de aprobación de alto riesgo: alert si diverge más del 10% del baseline
- Distribución de scores predichos: alert si la media móvil se desplaza más de 0.05
- Equidad entre segmentos: monitoreo mensual de métricas por zona geográfica y tipo de empleo

### Reentrenamiento Programado

Se recomienda reentrenar el modelo trimestralmente incorporando los datos más recientes de comportamiento de pago. El reentrenamiento debe incluir validación de que las nuevas versiones no introducen regresiones en métricas de equidad previamente establecidas.

## Próximos Pasos Inmediatos

1. **Validación con datos de producción**: ejecutar el modelo sobre las solicitudes de la última semana y comparar las predicciones con las decisiones tomadas por el equipo actual.

2. **Integración con sistemas core**: desarrollar la conexión API entre el modelo y el sistema de originación de préstamos para flujo automatizado.

3. **Capacitación del equipo**: entrenar a los analistas de crédito en la interpretación de las puntuaciones del modelo y los protocolos de override documentado.

4. **Definición de políticas de riesgo**: establecer los criterios específicos de aprobación, revisión manual y rechazo basados en los scores del modelo y la tolerancia al riesgo definida por el comité de crédito.

## Conclusión

El modelo de predicción de mora temprana representa una mejora significativa respecto a los métodos tradicionales de evaluación crediticia. Con un AUC-ROC de 0.891 y la capacidad de identificar correctamente al 72% de los clientes de alto riesgo, el modelo permite a FintechBank reducir las pérdidas por mora mientras mantiene una experiencia de aprobación eficiente para clientes calificados.

La implementación gradual, el monitoreo continuo y el reentrenamiento periódico son esenciales para mantener los beneficios del modelo a lo largo del tiempo. El éxito del proyecto dependerá de la colaboración efectiva entre los equipos de ciencia de datos, riesgo crediticio y tecnología de la información.

---
*Documento preparado para el Comité de Dirección de FintechBank - Unidad de Riesgos Crediticios*