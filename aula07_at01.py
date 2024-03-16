import openpyxl

'''

Atividade juntar as informaçoes de duas planilhas (categorias e porduto)
    - Abrir o primeiro arquivo CSV
    - guardar as infor de 1° arquivo CSV
    - Abrir o segundo arquivo CSV
    - Guardar as infor do 2° arquivo CSV
    - Mescla / tratar as informaçoes com os valores correspondente
    - Manter somente as info necessaria
    - Converter as info para o xlsx

'''

def CarregarArquivoCsv(nome_arquivo):
    dados_arquivo = open(nome_arquivo + '.csv', 'r', encoding='utf-8')

    lista_info = [] # -> array vazio
    for linha in dados_arquivo:
        colunas = linha.strip().split(';')
        lista_info.append(colunas)
    
    return lista_info 


def ConcatenarArquivosCsv(categoriasCSV, produtosCSV):
    dados_csv = []
    dados_csv.append([
        'id-produto',
        'nome_produto',
        'quantidade',
        'valor_venda',
        'valor_compra',
        'id_categoria',
        'nome_categoria'
    ])
    for produto in produtosCSV:
        index = int(produto[2]) -1
        #dados_csv.append([*produto, *categoriasCSV[index]])
        dados_csv.append([
            produto[0],
            produto[1],
            produto[4],
            produto[8],
            produto[9],
            categoriasCSV[index][0],
            categoriasCSV[index][1]
        ])

    return dados_csv    

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


dados_categoria = CarregarArquivoCsv('categorias')
dados_produtos = CarregarArquivoCsv('produtos')
dados_concatenados = ConcatenarArquivosCsv(dados_categoria, dados_produtos)

GravarArquivoXLSX(dados_concatenados, 'info_tratadas')

