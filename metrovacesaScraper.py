import requests
from bs4 import BeautifulSoup


# Comenzamos con la web de una promoción. Posteriormente habrá que abrir el espectro a las demás (y la forma de recuperarlas)
str = "https://metrovacesa.com/promociones/alicante/alicante-alacant/edificio-adamar"

page = requests.get(str)
soup = BeautifulSoup(page.content)
trs = soup.findAll('tr')
contador = 0

for tr in trs:
    
    contador = contador+1
    if contador == 2:
        print(tr.descendants)
        break


# print(trs)
# print(soup.prettify())
# print(soup.getText())

