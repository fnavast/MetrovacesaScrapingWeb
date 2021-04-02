# MetrovacesaScrappingWeb

La funcionalidad del script es almacenar en un fichero csv las características de las viviendas de las diferentes promociones con las que cuenta el grupo inmobiliario Metrovacesa.

Para ejecutar el script es necesario instalar las bibliotecas incluidas en el fichero requeriments.txt

```
pip install -r requirements.txt
```

Después de instalar las librerías necesarias, el script se ejecuta con el siguiente comando:

```
python metrovacesaScraper.py
```

El resultado del script se almacena en el fichero metrovacesa.csv. Este fichero presenta los siguientes campos:
* provincia: provincia en la que se encuentra el inmueble.
* localidad: localidad en la que está ubicada la vivienda.
* promocion: nombre comercial de la promoción. 
* viviendas: nombre comercial del inmueble dentro de la promoción.
* planta: número de planta en la que se encuentra la vivienda.
* dormitorios: número de dormitorios de los que dispone la vivienda.
* banos: número de baños de los que dispone el inmueble.
* superficie: superficie total en m2 del inmueble.
* terraza: superficie en m2 de la terraza.
* precio: precio en € de la vivienda.
