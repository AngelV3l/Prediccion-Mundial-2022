# ⚽ Predicción del Mundial de Fútbol 2022 con Python y Modelos de Poisson

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-lightgrey)](https://pandas.pydata.org/)
[![Project Type](https://img.shields.io/badge/Type-End_to_End_Project-green)]()
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen)]()

## 🧠 Descripción del proyecto

Este proyecto realiza una **predicción completa del Mundial de Fútbol 2022** utilizando un modelo probabilístico basado en la **distribución de Poisson**, partiendo de datos reales de todos los mundiales desde 1930. Está estructurado como un **proyecto de ciencia de datos de principio a fin**, que incluye:

- **Scraping y tratamiento de datos reales** desde Wikipedia.
- **Limpieza y transformación de datasets** con pandas.
- **Análisis exploratorio** y visualizaciones descriptivas.
- **Diseño e implementación de un modelo predictivo probabilístico**.
- **Simulación completa del torneo**, incluyendo fase de grupos y eliminatorias.

Este proyecto combina técnicas estadísticas sólidas con habilidades prácticas de programación y análisis de datos, y está orientado a demostrar competencias clave en **data science aplicada, modelado predictivo, simulación estadística** y storytelling técnico.

## 🎯 Objetivos

- Recolectar datos históricos del Mundial mediante scraping y limpieza.
- Analizar y visualizar estadísticas clave del torneo.
- Estimar la "fuerza" ofensiva y defensiva de cada selección.
- Implementar un modelo predictivo usando la distribución de Poisson.
- Simular el desarrollo completo del torneo y predecir un ganador.

## 🛠️ Tecnologías y herramientas utilizadas

| Herramienta          | Descripción                                       |
|----------------------|---------------------------------------------------|
| **Python**           | Lenguaje principal para análisis y modelado       |
| **Pandas**           | Manipulación y limpieza de datos                  |
| **Matplotlib / Seaborn** | Visualización de datos                       |
| **Scipy**            | Distribución de Poisson para modelado probabilístico |
| **Jupyter Notebook** | Entorno de desarrollo y presentación interactiva  |
| **Git / GitHub**     | Control de versiones y publicación del proyecto   |

## 📂 Estructura del repositorio

```
├── grupos_mundial2022.ipynb       # Extracción y visualización de estadísticas del Mundial
├── limpieza_datos.ipynb           # Proceso de limpieza y transformación de datos
├── modelo.ipynb                   # Modelo Poisson y simulación completa del Mundial
├── dict_table                     # Estructura de grupos usada en el modelo (pickle)
├── clean_fifa_worldcup_historical_data.csv   # Datos históricos limpios
├── clean_fifa_worldcup_fixture.csv           # Fixture del Mundial 2022 limpio
├── README.md                      # Este archivo
```

## 📊 Resultados del modelo

El modelo predice partido a partido utilizando la esperanza de goles de cada equipo, y a partir de ahí asigna puntos. Se simula todo el torneo, obteniendo las posiciones de grupos y ganadores de cada ronda eliminatoria.

> ✅ El enfoque está basado en datos objetivos y es completamente reproducible.

## 🧩 Posibles mejoras

- Usar modelos de Machine Learning supervisado (e.g. XGBoost, Logistic Regression).
- Incorporar rankings FIFA o resultados recientes como variables adicionales.
- Simular múltiples veces (Monte Carlo) para estimar probabilidades de victoria más realistas.
- Aplicar modelos bayesianos o mixturas para refinar la estimación de goles.

## 🚀 Lo que demuestra este proyecto

Este proyecto refleja habilidades clave que buscan empresas en roles de Data Analyst, Data Scientist y consultoría analítica:

- Dominio de **pandas, visualización y modelado estadístico**.
- Capacidad para resolver un problema real de principio a fin.
- Comunicación efectiva mediante notebooks bien documentados.
- **Pensamiento analítico y uso de modelos probabilísticos aplicados.**
- Creatividad para aplicar ciencia de datos en contextos atractivos (como el fútbol).

## 🧑‍💼 Sobre mí

Este proyecto forma parte de mi portfolio como científico de datos. Si estás buscando a alguien con formación matemática sólida, pasión por los datos y capacidad para resolver problemas reales, estaré encantado de conectar contigo. Puedes contactarme por [LinkedIn](https://www.linkedin.com/) o consultar otros proyectos en este perfil.

## 📥 Cómo usar este repositorio

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/mundial2022_poisson.git
   cd mundial2022_poisson
   ```
2. Instala las dependencias:
   ```bash
   pip install pandas matplotlib seaborn scipy
   ```
3. Abre los notebooks en JupyterLab o VSCode y explora las secciones paso a paso.

## 📌 Notas finales

- Este proyecto se desarrolló únicamente con datos públicos disponibles en Wikipedia.
- No representa predicciones oficiales ni busca precisión comercial.
- Es una demostración educativa del uso de estadística y Python para resolver un problema divertido y complejo.