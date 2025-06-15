from bs4 import BeautifulSoup
import requests
import pandas as pd

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978,
         1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]

#Funcion para extraer partidos de un mundial
def get_matches(year):
    #Web scrapping para obtener los partidos del mundial
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    #Extraemos todos los contenedores de partidos
    matches = soup.find_all('div', class_='footballbox')

    home = []
    score = []
    away = []

    #Extraemos y almacenamos de cada partido equipos y resultado
    for match in matches:
     home.append(match.find('th', class_= 'fhome').get_text())
     score.append(match.find('th', class_='fscore').get_text())
     away.append(match.find('th', class_='faway').get_text())

    #Almacenamos los partidos en un dataframe
    dict_football = {'home': home, 'score': score, 'away':away}
    df_football = pd.DataFrame(dict_football)
    #Y añadimos una columna más para el año del mundial scrapeado
    df_football['year'] = year
    return df_football
 
#Exportamos  todos los partidos
fifa = [get_matches(year) for year in years] #Lista con todos los dataframes
df_fifa = pd.concat(fifa, ignore_index=True)  
df_fifa.to_csv('fifa_worldcup_historical_data.csv', index = False)



##Por último, extraemos también los partidos que se van a jugar en el mundial 2022
#df_fixture = get_matches('2022')
#df_fixture.to_csv('fifa_worldcup_fixture.csv', index = False)

#Nota: Descargo este archivo externo, al haber ocurrido ya el mundial, no están disponibles la estructura inicial