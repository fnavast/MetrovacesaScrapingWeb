import requests
from bs4 import BeautifulSoup
import logging
from datetime import datetime
import pandas as pd


def set_logger():
    logging.basicConfig(format='%(levelname)s - %(filename)s: %(message)s')
    logging.getLogger().setLevel(logging.INFO)


def extract_data(url):
    logging.info('Extracción de los datos de la url ' + url)

    # Columnas del dataframe de extracción
    column_names = ['provincia', 'localidad', 'promocion', 'viviendas', 'planta',
                    'dormitorios', 'banos', 'superficie', 'terraza', 'precio']
    df = pd.DataFrame(columns=column_names)

    index = 0
    response = requests.post(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracción de los campos provincia y localidad de la promoción
    div_location = soup.findAll('div', {'id': 'promo-container'})[0]
    provincia_poblacion = div_location.find('span').text.split(',')
    provincia = provincia_poblacion[0].strip().replace('\n', '').replace('\t', '')
    localidad = provincia_poblacion[1].strip().replace('\n', '').replace('\t', '')
    promocion = div_location.find('h1').text.strip().replace('\n', '').replace('\t', '')

    logging.info('Extrayendo la promoción ' + str(promocion) + ' de la localidad ' + str(localidad))
    try:
        # La promoción tiene varios tipos de viviendas
        table = soup.find('table')
        for row in table.findAll('tr'):
            # El primer elemento es la cabecera
            if index != 0:
                cells = row.findAll('td')
                viviendas = cells[0].text.strip().replace('\n', '').replace('\t', '')
                planta = cells[1].text.strip().replace('\n', '').replace('\t', '')
                dormitorios = cells[2].text.strip().replace('\n', '').replace('\t', '')
                banos = cells[3].text.strip().replace('\n', '').replace('\t', '')
                superficie = cells[4].text.strip().replace('\n', '').replace('\t', '')
                terraza = cells[5].text.strip().replace('\n', '').replace('\t', '')
                precio = cells[7].text.strip().replace('\n', '').replace('\t', '')

                data = [provincia, localidad, promocion, viviendas, planta, dormitorios, banos, superficie, terraza, precio]
                df.loc[index - 1] = data
            index += 1
    except:
        try:
            # La promoción no tiene varios tipos de viviendas
            div_caracteristicas = soup.findAll('div', {'id': 'promo-container'})[0]\
                .find('ul')\
                .findAll('li')
            viviendas = div_caracteristicas[0].text
            dormitorios = div_caracteristicas[2].text.split(' ')[0]
            superficie = div_caracteristicas[1].text.split(' ')[1]

            precio = soup.findAll('div', {'id': 'promo-container'})[0].findAll('h1')[1].text\
                .strip().replace('\n', '').replace('\t', '').replace('€', '')

            planta = ''
            banos = ''
            terraza = ''

            data = [provincia, localidad, promocion, viviendas, planta, dormitorios, banos, superficie, terraza, precio]
            df.loc[0] = data
        except:
            # TODO: revisar los casos que no se han podido mapear
            logging.error('No se puede recuperar la información de la url ' + str(url))

    return df

def save_data(df, filename):
    df.to_csv('../csv/' + filename + '.csv', index=False)
    logging.info('Se ha guardado el fichero ' + filename + '.csv')


def main(url_dir):
    # Inicialización del logger
    set_logger()

    # Inicio del proceso
    start_time = datetime.now()
    logging.info('Inicio del proceso datetime: ' + str(start_time.strftime('%Y-%m-%d %H:%M:%S')))
    logging.info('Extracción del dataset metrovacesa de la url ' + url_dir)

    # Declaramos la url principal y el array donde almacenaremos todos los links que necesitamos
    links = []

    #Obtenemos el DOM de la url principal
    page = requests.get(url_dir)
    soup = BeautifulSoup(page.content)

    # Nos quedamos con el tag con id "provincias" que es donde se encuentran los links de cada provincia
    provincias = soup.findAll(id="provincias")

    #Recorremos cada web de provincia para recuperar los links de las promociones
    for link in provincias[0].findAll("a"):
        page = requests.get(link.get('href'))
        pv = BeautifulSoup(page.content)
        promociones = pv.findAll(id="cartas-promociones")
        for link in promociones[0].findAll("a"):
            # Si el link de la promoción no está vacío lo insertamos en el array
            if link.get('href') != '':
                links.append(link.get('href'))

    # Definimos el dataframe final que guardaremos en un fichero csv
    df_final = pd.DataFrame()

    # Recorremos los links de las promociones extrayendo la información
    for url_dir in links:
        # LLamada el metodo de extracción de la información
        df_data = extract_data(url_dir)
        df_final = pd.concat([df_final, df_data])
    save_data(df_final, 'metrovacesa')

    # Fin del proceso
    end_time = datetime.now()
    logging.info('Fin del proceso datetime: ' + str(end_time.strftime('%Y-%m-%d %H:%M:%S')))
    logging.info('Duración del proceso datetime: ' + str(round((end_time - start_time).seconds/60, 2)) + ' minutos')


if __name__ == "__main__":
    url_dir = 'https://metrovacesa.com/'
    main(url_dir)
