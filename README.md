# MetrovacesaScrappingWeb

## Miembros del equipo
El código ha sido desarrollado por:
* **Francisco de Borja Navas Torres**
* **Alvaro de la Fuente Díaz**

## Descripción de los ficheros
En el repositorio están almecenados los siguientes ficheros:
* **csv/metrovacesa.csv**: dataset generado a través del proceso.
* **pdf/metrovacesa.pdf**: fichero que contiene tanto la descripción del proceso de web scraping como la  información referente al dataset generado.
* **src/metrovacesaScraper.py**: código fuente encargado de realizar el proceso de web scraping.
* **test/test_metrovacesaScraper.py**: fichero de código utilizado durante la codificación del código fuente para realizar test en local.
* **README.md**: wiki del repositorio git.
* **requirements.txt**: librerias necesarias para poder ejecutar el proceso de web scraping.

## Descripción del proceso
La funcionalidad del script es almacenar en un fichero csv las características de las viviendas de las diferentes promociones con las que cuenta el grupo inmobiliario Metrovacesa.

Para ejecutar el script es necesario instalar las bibliotecas incluidas en el fichero requeriments.txt

```
pip install -r requirements.txt
```

Después de instalar las librerías necesarias, el script se ejecuta con el siguiente comando:

```
python metrovacesaScraper.py
```

## Descripción del dataset
El resultado del script se almacena en el fichero metrovacesa.csv. Este fichero esta almacenado en el repositorio de datos Zenodo con el siguiente DOI: 10.5281/zenodo.4678321
También se puede acceder a el a través del enlace https://doi.org/10.5281/zenodo.4678321

El dataset está formado por los siguientes campos:
* **provincia**: provincia en la que se encuentra la promoción.
* **localidad**: localidad en la que se encuentra la promoción.
* **promocion**: nombre comercial de la promoción.
* **viviendas**: tipo de vivienda dentro de la promoción.
* **planta**: planta en la que se encuentra la vivienda.
* **dormitorios**: número de dormitorios de la vivienda.
* **baños**: número de baños de la vivienda.
* **superficie**: superficie expresada en metros cuadrados de la vivienda.
* **terraza**: superficie expresada en metros cuadrados de la terraza de la vivienda.
* **precio**: precio de la vivienda.
* **observacion**: comentarios adicionales. Por ejemplo, hay promociones que han sido publicadas pero sin datos sobre ellas al ser muy recientes. Para estos casos en este campo se incluye “Promoción disponible próximamente”.
* **fecha_extraccion**: fecha en la que se ha realizado la extracción de la información.
