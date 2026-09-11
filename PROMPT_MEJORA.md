# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Archivos que la arquitectura del reto declara y no estan

Creálos con implementacion real, en la capa que les corresponde:

- `src/models/train_model.py`
- `src/models/evaluate_model.py`
- `tests/test_data_quality.py`

## Como saber que terminaste

```bash
pip install -r requirements.txt && pytest -q
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Ciencia de Datos, Especialidad Cientifico de datos, Tecnología scikit-learn, Advanced

### Brecha de conocimiento
Construye modelos evitando fuga de informacion y reporta metricas interpretadas en terminos del negocio

### Misión / candidato
Predecir el riesgo de mora temprana

### Reto
- Tema: Modelos de clasificación y su evaluación
- Seniority: advanced-l3
- Tipo: practical
- Título: Predicción de riesgo de mora temprana
- Tiempo estimado: 15 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Exploración y preparación de datos — objetivo: Comprender la estructura y calidad de los datos disponibles para la predicción. — entregable (NO resolver): Documento de exploración de datos que incluye hallazgos y recomendaciones.
- Fase 2: Construcción del modelo — objetivo: Construir un modelo de clasificación que evite la fuga de información. — entregable (NO resolver): Modelo de clasificación entrenado y ajustado, junto con un informe de evaluación.
- Fase 3: Interpretación y presentación de resultados — objetivo: Interpretar y presentar los resultados del modelo en términos del negocio. — entregable (NO resolver): Informe ejecutivo que incluye la interpretación de los resultados, identificación de sesgos o limitaciones, y recomendaciones.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: pyproject.toml ===
[tool.poetry]
name = "fintechbank-mora-temprana"
version = "0.1.0"
description = "Modelo de clasificación para predicción de riesgo de mora temprana en préstamos personales"
authors = ["Data Science Team <ds-team@fintechbank.com>"]
readme = "README.md"
packages = [{include = "src", from = "."}]

[tool.poetry.dependencies]
python = "^3.13"
scikit-learn = "1.5.0"
pandas = "2.2.2"
numpy = "1.26.4"
matplotlib = "3.9.0"
seaborn = "0.13.2"
jupyter = "1.0.0"
statsmodels = "0.14.2"
imbalanced-learn = "0.12.3"

[tool.poetry.group.dev.dependencies]
pytest = "8.2.0"
poetry = "1.8.0"

[tool.poetry.group.test.dependencies]
pytest = "8.2.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-q --tb=short"

[tool.poetry.scripts]
train-model = "src.models.train_model:main"
evaluate-model = "src.models.evaluate_model:main"


// === ARCHIVO: notebooks/eda.ipynb ===
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["# Análisis Exploratorio de Datos: Predicción de Mora Temprana\n",\n **FintechBank - Préstamos Personales**\n",\n "---\n",\n "Este notebook documenta el análisis exploratorio de datos para el modelo de predicción de riesgo de mora temprana.\n",\n "Se analizan distribuciones, correlaciones, valores faltantes y atípicos."]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": ["# Importación de librerías\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import os\n",
    "import sys\n",
    "from pathlib import Path\n",
    "\n",
    "# Configuración de visualizaciones\n",
    "plt.style.use('seaborn-v0_8-whitegrid')\n",
    "sns.set_palette('husl')\n",
    "%matplotlib inline\n",
    "\n",
    "# Agregar src al path\n",
    "sys.path.append(str(Path('../src').resolve()))"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 1. Carga de Datos"]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": ["# Carga del dataset\n",
    "data_path = Path('../data/raw/loan_data.csv')\n",
    "\n",
    "try:\n",
    "    df = pd.read_csv(data_path)\n",
    "    print(f"Dataset cargado exitosamente: {df.shape[0]} filas, {df.shape[1]} columnas")\n",
    "except FileNotFoundError:\n",
    "    print(\"Archivo no encontrado. Generando datos sintéticos para demostración...\")\n",
    "    # Generación de datos sintéticos para el dominio de mora temprana\n",
    "    np.random.seed(42)\n",
    "    n_samples = 5000\n",
    "    \n",
    "    df = pd.DataFrame({\n",
    "        'loan_id': range(1, n_samples + 1),\n",
    "        'age': np.random.randint(18, 70, n_samples),\n",
    "        'income': np.random.lognormal(10.5, 0.5, n_samples),\n",
    "        'employment_years': np.random.exponential(5, n_samples),\n",
    "        'credit_score': np.random.randint(300, 850, n_samples),\n",
    "        'loan_amount': np.random.lognormal(9.5, 0.8, n_samples),\n",
    "        'loan_term': np.random.choice([12, 24, 36, 48, 60], n_samples),\n",
    "        'interest_rate': np.random.uniform(5.0, 25.0, n_samples),\n",
    "        'debt_to_income': np.random.uniform(0.05, 0.6, n_samples),\n",
    "        'existing_loans': np.random.poisson(1.5, n_samples),\n",
    "        'payment_behavior': np.random.choice(['on_time', 'late', 'early'], n_samples, p=[0.6, 0.25, 0.15]),\n",
    "        'employment_type': np.random.choice(['full_time', 'part_time', 'self_employed', 'unemployed'], n_samples, p=[0.5, 0.2, 0.2, 0.1]),\n",
    "        'education': np.random.choice(['high_school', 'bachelor', 'master', 'phd'], n_samples, p=[0.3, 0.4, 0.2, 0.1]),\n",
    "        'marital_status': np.random.choice(['single', 'married', 'divorced', 'widowed'], n_samples, p=[0.35, 0.45, 0.15, 0.05]),\n",
    "        'home_ownership': np.random.choice(['rent', 'own', 'mortgage'], n_samples, p=[0.4, 0.25, 0.35]),\n",
    "        'early_default': np.random.choice([0, 1], n_samples, p=[0.78, 0.22])\n",
    "    })\n",
    "    \n",
    "    # Introducir valores faltantes (simulando datos reales)\n",
    "    missing_indices = np.random.choice(n_samples, size=int(n_samples * 0.05), replace=False)\n",
    "    df.loc[missing_indices[:int(n_samples * 0.02)], 'employment_years'] = np.nan\n",
    "    missing_indices_2 = np.random.choice(n_samples, size=int(n_samples * 0.03), replace=False)\n",
    "    df.loc[missing_indices_2, 'income'] = np.nan\n",
    "    \n",
    "    print(f"Datos sintéticos generados: {df.shape[0]} filas, {df.shape[1]} columnas")"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 2. Estructura y Tipos de Datos"]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": ["# Información general del dataset\n",
    "print(\"=== INFORMACIÓN DEL DATASET ===\n\")\n",
    "df.info()\n",
    "\n",
    "print(\"\n=== PRIMERAS 5 FILAS ===\")\n",
    "df.head()"]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": ["# Estadísticas descriptivas de variables numéricas\n",
    "print(\"=== ESTADÍSTICAS DESCRIPTIVAS ===\")\n",
    "df.describe().T"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 3. Valores Faltantes"]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": ["# Análisis de valores faltantes\n",
    "missing_analysis = pd.DataFrame({\n",
    "    'columna': df.columns,\n",
    "    'tipo': df.dtypes.values,\n",
    "    'total': len(df),\n",
    "    'faltantes': df.isnull().sum().values,\n",
    "    'porcentaje_faltante': (df.isnull().sum() / len(df) * 100).values\n",
    "})\n",
    "missing_analysis = missing_analysis[missing_analysis['faltantes'] > 0].sort_values('porcentaje_faltante', ascending=False)\n",
    "\n",
    "print(\"=== VALORES FALTANTES ===\")\n",
    "if len(missing_analysis) > 0:\n",
    "    print(missing_analysis.to_string(index=False))\n",
    "else:\n",
    "    print(\"No se detectaron valores faltantes.\")"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 4. Distribución de la Variable Objetivo"]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": ["# Distribución de la variable objetivo\n",
    "target_dist = df['early_default'].value_counts()\n",
    "target_pct = df['early_default'].value_counts(normalize=True) * 100\n",
    "\n",
    "print(\"=== DISTRIBUCIÓN DE LA VARIABLE OBJETIVO ===\")\n",
    "print(f\"No Mora (0): {target_dist[0]} ({target_pct[0]:.2f}%)\")\n",
    "print(f\"Mora Temprana (1): {target_dist[1]} ({target_pct[1]:.2f}%)\")\n",
    "\n",
    "# Visualización\n",
    "fig, ax = plt.subplots(figsize=(8, 5))\n",
    "colors = ['#2ecc71', '#e74c3c']\n",
    "bars = ax.bar(['No Mora', 'Mora Temprana'], [target_dist[0], target_dist[1]], color=colors, edgecolor='black')\n",
    "ax.set_ylabel('Frecuencia', fontsize=12)\n",
    "ax.set_title('Distribución de Mora Temprana en Préstamos', fontsize=14, fontweight='bold')\n",
    "for bar, pct in zip(bars, [target_pct[0], target_pct[1]]):\n",
    "    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50, \n",
    "            f'{pct:.1f}%', ha='center', va='bottom', fontsize=11)\n",
    "plt.tight_layout()\n",
    "plt.savefig('../reports/figures/target_distribution.png', dpi=150)\n",
    "plt.show()"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 5. Análisis de Variables Numéricas"]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": ["# Identificar columnas numéricas\n",
    "numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()\n",
    "numeric_cols = [c for c in numeric_cols if c not in ['loan_id', 'early_default']]\n",
    "\n",
    "print(f\"Variables numéricas para análisis: {numeric_cols}\")\n",
    "\n",
    "# Histogramas\n",
    "fig, axes = plt.subplots(3, 3, figsize=(14, 12))\n",
    "axes = axes.flatten()\n",
    "\n",
    "for idx, col in enumerate(numeric_cols):\n",
    "    if idx < len(axes):\n",
    "        # Histograma por clase\n",
    "        for label, color, name in [(0, '#2ecc71', 'No Mora'), (1, '#e74c3c', 'Mora')]:\n",
    "            subset = df[df['early_default'] == label][col].dropna()\n",
    "            axes[idx].hist(subset, bins=30, alpha=0.5, label=name, color=color, density=True)\n",
    "        axes[idx].set_title(f'Distribución: {col}', fontsize=11)\n",
    "        axes[idx].legend(fontsize=8)\n",
    "        axes[idx].set_xlabel(col)\n",
    "        axes[idx].set_ylabel('Densidad')\n",
    "\n",
    "# Ocultar subplots vacíos\n",
    "for idx in range(len(numeric_cols), len(axes)):\n",
    "    axes[idx].set_visible(False)\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.savefig('../reports/figures/numeric_distributions.png', dpi=150)\n",
    "plt.show()"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 6. Análisis de Variables Categóricas"]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": ["# Identificar columnas categóricas\n",
    "categorical_cols = df.select_dtypes(include=['object']).columns.tolist()\n",
    "\n",
    "print(f\"Variables categóricas: {categorical_cols}\")\n",
    "\n",
    "# Distribución y tasa de mora por categoría\n",
    "fig, axes = plt.subplots(2, 2, figsize=(14, 10))\n",
    "axes = axes.flatten()\n",
    "\n",
    "for idx, col in enumerate(categorical_cols[:4]):\n",
    "    # Tasa de mora por categoría\n",
    "    default_rate = df.groupby(col)['early_default'].mean().sort_values(ascending=False)\n",
    "    \n",
    "    bars = axes[idx].bar(range(len(default_rate)), default_rate.values, color='#3498db', edgecolor='black')\n",
    "    axes[idx].set_xticks(range(len(default_rate)))\n",
    "    axes[idx].set_xticklabels(default_rate.index, rotation=45, ha='right')\n",
    "    axes[idx].set_ylabel('Tasa de Mora')\n",
    "    axes[idx].set_title(f'Tasa de Mora por {col}', fontsize=11, fontweight='bold')\n",
    "    axes[idx].axhline(y=df['early_default'].mean(), color='red', linestyle='--', label='Tasa global')\n",
    "    axes[idx].legend()\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.savefig('../reports/figures/categorical_analysis.png', dpi=150)\n",
    "plt.show()"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 7. Análisis de Correlaciones"]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": ["# Matriz de correlación\n",
    "numeric_df = df[numeric_cols + ['early_default']].copy()\n",
    "corr_matrix = numeric_df.corr()\n",
    "\n",
    "# Heatmap\n",
    "fig, ax = plt.subplots(figsize=(12, 10))\n",
    "mask = np.triu(np.ones_like(corr_matrix, dtype=bool))\n",
    "sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r', \n",
    "            center=0, square=True, linewidths=0.5, ax=ax,\n    "            cbar_kws={'shrink': 0.8})\n",
    "ax.set_title('Matriz de Correlación - Variables Numéricas', fontsize=14, fontweight='bold')\n",
    "plt.tight_layout()\n",
    "plt.savefig('../reports/figures/correlation_matrix.png', dpi=150)\n",
    "plt.show()\n",
    "\n",
    "# Correlaciones con la variable objetivo\n",
    "print(\"=== CORRELACIONES CON VARIABLE OBJETIVO ===\")\n",
    "target_corr = corr_matrix['early_default'].drop('early_default').sort_values(key=abs, ascending=False)\n",
    "print(target_corr.to_string())"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 8. Detección de Valores Atípicos"]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": ["# Detección de atípicos usando IQR\n",
    "def detect_outliers_iqr(data, column):\n",
    "    Q1 = data[column].quantile(0.25)\n",
    "    Q3 = data[column].quantile(0.75)\n",
    "    IQR = Q3 - Q1\n",
    "    lower_bound = Q1 - 1.5 * IQR\n",
    "    upper_bound = Q3 + 1.5 * IQR\n",
    "    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)][column]\n",
    "    return len(outliers), lower_bound, upper_bound\n",
    "\n",
    "print(\"=== DETECCIÓN DE ATÍPICOS (IQR) ===\")\n",
    "outlier_summary = []\n",
    "\n",
    "for col in numeric_cols:\n",
    "    count, lower, upper = detect_outliers_iqr(df, col)\n",
    "    pct = count / len(df) * 100\n",
    "    outlier_summary.append({\n",
    "        'variable': col,\n",
    "        'atipicos': count,\n",
    "        'porcentaje': pct,\n",
    "        'limite_inferior': lower,\n",
    "        'limite_superior': upper\n",
    "    })\n",
    "\n",
    "outlier_df = pd.DataFrame(outlier_summary)\n",
    "print(outlier_df.to_string(index=False))\n",
    "\n",
    "# Boxplots\n",
    "fig, axes = plt.subplots(2, 3, figsize=(14, 8))\n",
    "axes = axes.flatten()\n",
    "\n",
    "for idx, col in enumerate(numeric_cols[:6]):\n",
    "    df.boxplot(column=col, by='early_default', ax=axes[idx])\n",
    "    axes[idx].set_title(f'{col} por Mora')\n",
    "    axes[idx].set_xlabel('Mora Temprana')\n",
    "\n",
    "plt.suptitle('Detección de Atípicos', fontsize=14, fontweight='bold', y=1.02)\n",
    "plt.tight_layout()\n",
    "plt.savefig('../reports/figures/outliers_boxplot.png', dpi=150)\n",
    "plt.show()"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 9. Análisis Multivariado"]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": ["# Scatter: Ingreso vs Score Crediticio por clase\n",
    "fig, ax = plt.subplots(figsize=(10, 6))\n",
    "\n",
    "for label, color, name in [(0, '#2ecc71', 'No Mora'), (1, '#e74c3c', 'Mora')]:\n",
    "    subset = df[df['early_default'] == label]\n",
    "    ax.scatter(subset['income'], subset['credit_score'], alpha=0.4, 
",
    "               c=color, label=name, s=20)\n",
    "\n",
    "ax.set_xlabel('Ingreso', fontsize=12)\n",
    "ax.set_ylabel('Score Crediticio', fontsize=12)\n",
    "ax.set_title('Ingreso vs Score Crediticio por Mora Temprana', fontsize=14, fontweight='bold')\n",
    "ax.legend()\n",
    "plt.tight_layout()\n",
    "plt.savefig('../reports/figures/scatter_income_credit.png', dpi=150)\n",
    "plt.show()"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 10. Hallazgos y Recomendaciones"]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": ["# Resumen de hallazgos\n",
    "print(\"=== HALLAZGOS PRINCIPALES ===\n\")\n",
    "\n",
    "print(\"1. DISTRIBUCIÓN DE LA VARIABLE OBJETIVO:\")\n",
    "print(f\"   - La tasa de mora temprana es {target_pct[1]:.2f}% (clase desbalanceada)\")\n",
    "print(\"   - Se requiere técnicas de balanceo para el modelado\n\")\n",
    "\n",
    "print(\"2. VALORES FALTANTES:\")\n",
    "if len(missing_analysis) > 0:\n",
    "    for _, row in missing_analysis.iterrows():\n",
    "        print(f\"   - {row['columna']}: {row['porcentaje_faltante']:.2f}% (imputar con mediana/moda)\")\n",
    "else:\n",
    "    print(\"   - No se detectaron valores faltantes significativos\")\n",
    "\n",
    "print(\"\n3. CORRELACIONES IMPORTANTES CON MORA:\")\n",
    "top_corr = target_corr.head(5)\n",
    "for var, corr in top_corr.items():\n",
    "    direction = 'positiva' if corr > 0 else 'negativa'\n",
    "    print(f\"   - {var}: correlación {direction} ({corr:.3f})\")\n",
    "\n",
    "print(\"\n4. VARIABLES CATEGÓRICAS CON MAYOR IMPACTO:\")\n",
    "for col in categorical_cols[:3]:\n",
    "    rates = df.groupby(col)['early_default'].mean()\n",
    "    max_cat = rates.idxmax()\n",
    "    print(f\"   - {col}: categoría '{max_cat}' con mayor tasa de mora ({rates[max_cat]:.2%})\")\n",
    "\n",
    "print(\"\n5. RECOMENDACIONES PARA MODELADO:\")\n",
    "print(\"   - Aplicar SMOTE o undersampling para balancear clases\")\n",
    "print(\"   - Imputar valores faltantes: mediana para numéricas, moda para categóricas\")\n",
    "print(\"   - Considerar transformación logarítmica para variables sesgadas\")\n",
    "print(\"   - Examinar interacción entre income, credit_score y debt_to_income\")"]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": ["# Guardar datos procesados para siguientes etapas\n",
    "os.makedirs('../data/processed', exist_ok=True)\n",
    "df.to_csv('../data/processed/loan_data_cleaned.csv', index=False)\n",
    "print(\"Datos guardados en: ../data/processed/loan_data_cleaned.csv\")"]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
// === ARCHIVO: src/data/load_data.py ===
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
// === ARCHIVO: src/features/build_features.py ===
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


// === ARCHIVO: src/serve/predict.py ===
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


// === ARCHIVO: tests/test_model_metrics.py ===
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


// === ARCHIVO: tests/test_feature_engineering.py ===
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


// === ARCHIVO: reports/exploratory_analysis.md ===
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

// === ARCHIVO: reports/model_evaluation.md ===
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

// === ARCHIVO: reports/executive_summary.md ===
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

```
