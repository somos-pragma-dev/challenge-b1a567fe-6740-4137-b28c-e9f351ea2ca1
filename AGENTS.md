# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Predicción de riesgo de mora temprana**.

| | |
|---|---|
| Tema | Modelos de clasificación y su evaluación |
| Nivel | advanced-l3 |
| Chapter | Ciencia de Datos — Científico |
| Especialidad | Cientifico de datos |
| Stack | Python / scikit-learn 1.5.0 |
| Patron arquitectonico | Pipeline de machine learning con separación de responsabilidades (EDA, preprocesamiento, ingeniería de características, modelado, evaluación y despliegue) |
| Tiempo estimado | 15 horas |

## Tu tarea

Dejar este proyecto en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Corre `pip install -r requirements.txt && pytest -q` y mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `pip install -r requirements.txt && pytest -q` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Exploración y preparación de datos**: Documento de exploración de datos que incluye hallazgos y recomendaciones.
- **Fase 2 — Construcción del modelo**: Modelo de clasificación entrenado y ajustado, junto con un informe de evaluación.
- **Fase 3 — Interpretación y presentación de resultados**: Informe ejecutivo que incluye la interpretación de los resultados, identificación de sesgos o limitaciones, y recomendaciones.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Lo que falta y tenes que completar

### 1. Archivos que la arquitectura declara (3 de 13)

La propuesta arquitectonica del reto los lista y no llegaron al repo. Crealos con implementacion real, respetando la capa en la que viven:

- [ ] `src/models/train_model.py`
- [ ] `src/models/evaluate_model.py`
- [ ] `tests/test_data_quality.py`

### Presentes (10)

- `pyproject.toml`
- `notebooks/eda.ipynb`
- `src/data/load_data.py`
- `src/features/build_features.py`
- `src/serve/predict.py`
- `tests/test_model_metrics.py`
- `tests/test_feature_engineering.py`
- `reports/exploratory_analysis.md`
- `reports/model_evaluation.md`
- `reports/executive_summary.md`

### Capas del patron declarado

Cada una tiene que existir como directorio real con al menos un archivo. Codigo plano en la raiz no satisface el patron.

- `data/raw`
- `data/processed`
- `notebooks`
- `src/data`
- `src/features`
- `src/models`
- `src/serve`
- `tests`
- `reports`

## Verificacion

```bash
pip install -r requirements.txt && pytest -q
```

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- El patron es **Pipeline de machine learning con separación de responsabilidades (EDA, preprocesamiento, ingeniería de características, modelado, evaluación y despliegue)**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Perfil: Chapter Ciencia de Datos, Especialidad Cientifico de datos, Tecnología scikit-learn, Advanced
- Brecha que el reto ataca: Construye modelos evitando fuga de informacion y reporta metricas interpretadas en terminos del negocio
- Mision: Predecir el riesgo de mora temprana

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
