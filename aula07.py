import openpyxl

'''
# Atividade: converter o arquivo csv em xlsx
 #   - identificar o nome do arquivo csv -> ok  
 #  - abrir o arquivo -> ok
 #   - guardar as informaçoes do arquivo 
 #   - criar um novo arquivo xlsx (com o mesmo nome arquivo csv)
 #   - inserir as informaçoes guardadas no novo arquivo
'''

def CarregarArquivoCsv(nome_arquivo):
    dados_arquivo = open(nome_arquivo + '.csv', 'r', encoding='utf-8')

    lista_info = [] # -> array vazio
    for linha in dados_arquivo:
        colunas = linha.strip().split(';')
        lista_info.append(colunas)
    
    return lista_info 
    
def GravarArquivoXLSX(dados, nome_arquivo):
    try:
        excel = openpyxl.Workbook()  # -> Cria a estancia do excel
        planilha = excel.active # -> pega a primeira planilha disponivel 

        for linha in dados:
            planilha.append(linha)
        excel.save(nome_arquivo + '.xlsx')
        print('Dados salvo com sucesso no arquivo {} .xlsx'.format(nome_arquivo))
    except Exception as ex:
        print('Ocorreu um erro: {}'.format(ex))    



#nome_arquivo = input('Informe o nome de arquivo: ')
nome_arquivo = 'categorias'
dados_csv = CarregarArquivoCsv(nome_arquivo)
GravarArquivoXLSX(dados_csv, nome_arquivo)
