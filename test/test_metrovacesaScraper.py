from src.metrovacesaScraper import main as test_main

if __name__ == '__main__':
    # Comenzamos con la web de una promoción. Posteriormente habrá que abrir el espectro a las demás (y la forma de recuperarlas)
    url_dir = "https://metrovacesa.com/promociones/alicante/alicante-alacant/edificio-adamar"
    # url_dir = 'https://metrovacesa.com/'

    test_main(url_dir)



# # Comenzamos con la web de una promoción. Posteriormente habrá que abrir el espectro a las demás (y la forma de recuperarlas)
# str = "https://metrovacesa.com/promociones/alicante/alicante-alacant/edificio-adamar"
#
# page = requests.get(str)
# soup = BeautifulSoup(page.content)
# trs = soup.findAll('tr')
# contador = 0
#
# for tr in trs:
#
#     contador = contador+1
#     if contador == 2:
#         print(tr.descendants)
#         break


# print(trs)
# print(soup.prettify())
# print(soup.getText())

