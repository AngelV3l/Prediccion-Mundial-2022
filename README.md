# Predicción del Mundial 2022 con Modelos de Poisson
Este proyecto tiene como objetivo predecir los resultados del Mundial de Fútbol de la FIFA 2022 utilizando técnicas de ciencia de datos y modelos estadísticos. Se aplica un modelo de Poisson sobre datos históricos para simular partidos y estimar la clasificación final del torneo.

## Contenido
Extracción de datos desde Wikipedia usando Web Scraping

Limpieza y estructuración de los datos históricos y del fixture 2022

Modelado estadístico con Poisson para simular resultados

Visualización y análisis de las predicciones

## Estructura del Proyecto
notebooks/: Contiene los notebooks principales:

grupos_mundial2022.ipynb: Extracción de las tablas de grupos del Mundial 2022

limpieza_datos.ipynb: Limpieza de los datos históricos y del fixture

modelo.ipynb: Implementación del modelo Poisson y simulación del torneo

scripts/: Contiene el script para scrapear los partidos de los mundiales anteriores (scrape_matches.py)

data/: Almacena los datasets en formato CSV

## Cómo usar este repositorio
1. Clona el repositorio:

git clone https://github.com/tu_usuario/worldcup-prediction.git
cd worldcup-prediction

2. Instala las dependencias:

pip install -r requirements.txt

3. Ejecuta los notebooks paso a paso:

Primero, Tablas_Mundial2022.ipynb para cargar las tablas de grupos

Luego, ejecuta el script get_matches.py para descargar datos históricos

Después, Limpieza_de_datos.ipynb para limpiar y preparar los datos

Finalmente, Modelo.ipynb para construir y aplicar el modelo Poisson

## Librerías utilizadas
pandas
numpy
BeautifulSoup
requests

## Notas adicionales
El modelo de Poisson se entrena con datos de todos los mundiales anteriores.

Los resultados de los grupos del Mundial 2022 se simulan en base a la predicción de goles esperados.

El fixture original del Mundial 2022 ha sido limpiado y adaptado para simulaciones.

