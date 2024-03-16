from bs4 import BeautifulSoup
import requests

# def ConsultaSitePaquemenos(url):
#     resposta = requests.get(url)

#     if resposta.status_code == 200:
#        soup = BeautifulSoup(resposta.text, 'html.parser') 
#        page = soup.find('div', class_='list-products page-content')
#        print(page)


#        prod_paguemenos = []
#        for row in page.find_all('div', class_='desc position-relative'):
#            produto = row.find('h2').text.strip()
#            preco = row.find('p', class_='sale-price').text.strip()

#            prod_paguemenos.append([
#                produto,
#                preco
#            ])
           
#            return prod_paguemenos
    
        


#url = 'https://www.superpaguemenos.com.br/hortifruti/'
#ConsultaSitePaquemenos(url)



def ConsultaSiteSaovicente(url):
    resposta = requests.get(url)

    if resposta.status_code == 200:
       soup = BeautifulSoup(resposta.text, 'html.parser') 
       page = soup.find('div', class_='search-card-grid__container')
       print(page)


       


      



url = 'https://www.svicente.com.br/Hortifruti-3'  
ConsultaSiteSaovicente(url)