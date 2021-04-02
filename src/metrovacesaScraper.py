import requests
from bs4 import BeautifulSoup
import logging
from time import time, strftime
from datetime import datetime, timedelta
import pandas as pd


def set_logger():
    # logging.basicConfig(format='%(levelname)s - %(filename)s: %(message)s', level=logging.INFO)
    logging.basicConfig(format='%(levelname)s - %(filename)s: %(message)s')
    logging.getLogger().setLevel(logging.INFO)


def extract_data(url):
    column_names = ['viviendas', 'planta', 'dormitorios', 'banos', 'superficie', 'terraza', 'precio']
    df = pd.DataFrame(columns=column_names)
    index = 0
    response = requests.post(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    for row in table.findAll('tr'):
        if index != 0:
            cells = row.findAll('td')
            viviendas = cells[0].find(text=True)
            planta = cells[1].find(text=True)
            dormitorios = cells[2].find(text=True)
            banos = cells[3].find(text=True)
            superficie = cells[4].find(text=True)
            terraza = cells[5].find(text=True)
            precio = cells[7].find(text=True)

            data = [viviendas, planta, dormitorios, banos, superficie, terraza, precio]
            for i in range(len(data)):
                data[i] = data[i].strip().replace('\n', '').replace('\t', '')
            df.loc[index - 1] = data
        index += 1
    return df

def save_data(df, filename):
    df.to_csv('../csv/' + filename + '.csv', index=False)


def main(url_dir):
    # Calculamos las urls necesarias para obtener la información objetivo
    
    # Declaramos la url principal y el array donde almacenaremos todos los links que necesitamos
    str = "https://metrovacesa.com"
    links = []

    #Obtenemos el DOM de la url principal
    page = requests.get(str)
    soup = BeautifulSoup(page.content)

    # Nos quedamos con el tag con id "provincias" que es donde se encuentran los links de cada provincia
    provincias = soup.findAll(id="provincias")

    # Dentro del tag buscamos el tag a que es donde tenemos los links
    link = provincias[0].findAll("a")

    #Recorremos cada web de provincia para recuperar los links de las promociones
    for link in provincias[0].findAll("a"):

        page = requests.get(link.get('href'))
        pv = BeautifulSoup(page.content)
        promociones = pv.findAll(id="cartas-promociones")
        link = promociones[0].findAll("a")
        for link in promociones[0].findAll("a"):
            # Si el link de la promoción no está vacío lo insertamos en el array
            if link.get('href') != '':
                links.append(link.get('href'))

    # Inicialización del logger
    set_logger()

    # Inicio del proceso
    start_time = datetime.now()
    logging.info('Inicio del proceso datetime: ' + str(start_time.strftime('%Y-%m-%d %H:%M:%S')))
    logging.info('Extracción del dataset metrovacesa de la url ' + url_dir)

    index = 0
    for url_dir in links:
        df_data = extract_data(url_dir)
        save_data(df_data, 'metrovacesa_adamar')
        index += 1

    end_time = datetime.now()
    logging.info('Fin del proceso datetime: ' + str(end_time.strftime('%Y-%m-%d %H:%M:%S')))
    logging.info('Duración del proceso datetime: ' + str(round((end_time - start_time).seconds/60, 2)) + ' minutos')


if __name__ == "__main__":
    url_dir = "https://metrovacesa.com/promociones/alicante/alicante-alacant/edificio-adamar"
    # url_dir = 'https://metrovacesa.com/'
    main(url_dir)
