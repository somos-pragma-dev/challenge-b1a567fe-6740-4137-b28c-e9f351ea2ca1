# Predicción de riesgo de mora temprana

El banco 'FintechBank' necesita predecir el riesgo de mora temprana en sus préstamos personales. Los datos disponibles incluyen información demográfica de los solicitantes, historial de pagos, y datos de comportamiento en otros productos financieros. El objetivo es construir un modelo de clasificación que evite la fuga de información y reporte métricas interpretadas en términos del negocio.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Modelos de clasificación y su evaluación |
| **Nivel** | advanced-l3 |
| **Tipo** | practical |
| **Tiempo estimado** | 15 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Exploración y preparación de datos

**Objetivo:** Comprender la estructura y calidad de los datos disponibles para la predicción.

**Tiempo estimado:** 5 horas

**Instrucciones:**

- Identifica y documenta las fuentes de datos disponibles.
- Realiza una exploración inicial de los datos para identificar posibles problemas de calidad.
- Documenta cualquier hallazgo relevante que pueda afectar la construcción del modelo.

**Entregable:** Documento de exploración de datos que incluye hallazgos y recomendaciones.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la importancia de la limpieza de datos en la construcción de modelos.
- Reflexiona sobre posibles sesgos en los datos y su impacto en el modelo.

</details>

### Fase 2: Construcción del modelo

**Objetivo:** Construir un modelo de clasificación que evite la fuga de información.

**Tiempo estimado:** 5 horas

**Instrucciones:**

- Selecciona las características relevantes para la predicción.
- Divide los datos en conjuntos de entrenamiento y prueba.
- Entrena y ajusta un modelo de clasificación.
- Evalúa el modelo utilizando métricas apropiadas.

**Entregable:** Modelo de clasificación entrenado y ajustado, junto con un informe de evaluación.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la importancia de la selección de características en la construcción del modelo.
- Reflexiona sobre las métricas más adecuadas para evaluar el rendimiento del modelo en términos del negocio.

</details>

### Fase 3: Interpretación y presentación de resultados

**Objetivo:** Interpretar y presentar los resultados del modelo en términos del negocio.

**Tiempo estimado:** 5 horas

**Instrucciones:**

- Interpreta las métricas del modelo en términos del negocio.
- Identifica y documenta posibles sesgos o limitaciones del modelo.
- Presenta los resultados y recomendaciones en un informe ejecutivo.

**Entregable:** Informe ejecutivo que incluye la interpretación de los resultados, identificación de sesgos o limitaciones, y recomendaciones.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la importancia de la interpretación de los resultados en términos del negocio.
- Reflexiona sobre posibles sesgos o limitaciones del modelo y cómo abordarlos.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es un modelo de clasificación y cuál es su objetivo en este contexto?
- **paraQueSirve**: ¿Para qué sirve la evaluación de modelos de clasificación en términos del negocio?
- **comoSeUsa**: ¿Cómo se usa un modelo de clasificación para predecir el riesgo de mora temprana?
- **erroresComunes**: ¿Cuáles son los errores comunes en la construcción y evaluación de modelos de clasificación?
- **queDecisionesImplica**: ¿Qué decisiones implica la construcción y evaluación de un modelo de clasificación en términos del negocio?

## Criterios de Evaluacion

- Construir un modelo de clasificación que evite la fuga de información.
- Evaluar el modelo utilizando métricas apropiadas e interpretar los resultados en términos del negocio.
- Identificar y documentar posibles sesgos o limitaciones del modelo.
- Presentar los resultados y recomendaciones en un informe ejecutivo.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r requirements.txt && pytest -q
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
