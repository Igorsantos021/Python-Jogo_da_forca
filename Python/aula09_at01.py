'''
    Descobrir a quantidade de paginas disponiveis 
    percorrer todas as paginas 
    todos os produtos
    pegar o nome do produto
    pegar o valor do produto
    pegar o fabricante 
    pegar a % de desconto de produto
    Salvar em um arquivo xlsx
'''

from bs4 import BeautifulSoup
import requests
import openpyxl





def ConsultarQuantidadePagina(url):
    resposta = requests.get(url)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        pagina = soup.find('div', class_='page-template') # -> Retorna o primeiro resultado
        div = pagina.find_all('div', class_='text-center pt-3') # -> Retorna todos os resultados
        div = div[-1].text
        qntd = div.split(' ')[-1]
        return qntd

def ConsultarProdutosPaginas(url):
    resposta = requests.get(url)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        pagina = soup.find('div', class_='list-products page-content')
        produtos = pagina.find_all('div', class_='desc position-relative')
        lista_produtos =[]
    
        for item in produtos:
            nome = item.find('h2', class_='title').text.strip()
            fabricante = item.find('span', class_='font-size-11 text-primary font-weight-bold').text.strip()
            
            if bool(item.find('p', class_='sale-price')):
                preco = item.find('p', class_='sale-price').text.strip()
            else:
                preco = 'Sem Estoque'

            if bool(item.find('span', class_='discount')):
                desc = item.find('span', class_='discount').text.strip()
            else:
                desc = ''    
            # string, int, float, bool (verdadeiro ou falso)

            #print(nome, '|', fabricante, '|', preco, '|', desc)


            lista_produtos.append([
                nome,
                fabricante,
                preco,
                desc  
            ])  
        return lista_produtos

def GravarArquivosXLSX(dados, nome_arquivo):
    try:
        excel = openpyxl.Workbook()
        planilha = excel.active

        for linha in dados:
            planilha.append(linha)

        excel.save(nome_arquivo + '.xlsx')
        print('Dados salvo com sucesso no arquivo {}.xlsx'.format(nome_arquivo))
    except Exception as ex:
        print('Error: {}'.format(ex))    

area = 'hortifruti'

url = 'https://www.superpaguemenos.com.br/{}/'.format(area)
qntd = ConsultarQuantidadePagina(url)
print(qntd, 'valor de paginas')

produtos = []
for i in range (1, int(qntd)+ 1):
    new_url = url + '?p=' + str(i)
    print(new_url)
    produtos = produtos + ConsultarProdutosPaginas(new_url)    
    
GravarArquivosXLSX(produtos, area)

