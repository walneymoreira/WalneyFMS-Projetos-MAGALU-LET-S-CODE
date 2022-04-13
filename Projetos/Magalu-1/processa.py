import json
import os.path
import sys
import operator

#from processa import obter_dados, menu
def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

#Opção 1 - Listar categorias 
def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    lstcategorias = []
    vcont = 0
    vcat = ''
    for i in range(len(dados)):
        vcategoria = dados[i]['categoria']
        if not vcategoria in lstcategorias:
            lstcategorias.append(vcategoria)
            vcont += 1
    print()
    print()
    print()
    print()
    print(f'**************Lista de categorias**************')        
    for i in range(len(lstcategorias)):
        print(f' Categoria {i+1} - {lstcategorias[i]}')
    print(f'Foram encontadas {vcont} categorias!')
    print()

    return lstcategorias

    ...
#Opção 2 - Listar produto de uma categoria
def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    lstprodcat = []
    vprod = ''
    vcont = 0
    vcat = categoria
    for i in range(len(dados)):
        vprod = dados[i]['id']
        if vcat == dados[i]['categoria']:
            lstprodcat.append(vprod)
            vcont += 1

    print()
    print()
    print('*************************************************************************************************************')
    print(f'*******************Lista dos produtos da categoria {vcat} existentes na base de dados:**********************\n')
    for i in range(len(lstprodcat)):
        print(f'{i+1} - {lstprodcat[i]} - {vcat}')
    print()
    print('*************************************************************************************************************')
    print(f'Nessa base de dados existem {(len(lstprodcat))} produtos cadastrados para a categoria {vcat}')    
    print('*************************************************************************************************************')
    print()
    print()

    return lstprodcat

    
    ...
    
#Opção 3 - Produto mais caro por categoria
def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    vpreco = 0
    vprecomaior = 0
    vid = ''
    vprod = ''
    vcont = 0
    vcat = categoria
    dicprecocatmaior = {}
    lstprecocat = []
    for i in range(len(dados)):
        vprod = dados[i]['id'] 
        vpreco = dados[i]['preco']
        if vcat == dados[i]['categoria']:
            lstprecocat.append((vprod, float(vpreco)))
            if vpreco > dados[(i+1)]['preco']:
                vid = dados[i]['id'] 
                vprecomaior = dados[i]['preco']
            vcont += 1

    lstvalor = []
    for i in range(len(lstprecocat)):
        lstvalor.append(lstprecocat[i][1])
    lstvalor_ordenada = sorted(lstvalor, reverse=True)
    vprecomaior = lstvalor_ordenada[0]
    for i in range(len(lstprecocat)):
        if vprecomaior == lstprecocat[i][1]:
            vid = lstprecocat[i][0]
            dicprecocatmaior = {'Produto': vid, 'Preço': vprecomaior}

    print()
    print('*************************************************************************************************************')
    print(f'O dicionário do preço maior por categoria é: \n{dicprecocatmaior}')
    print('*************************************************************************************************************')
    print(f'O produto com maior preço da categoria "({vcat})" é: "\n({vid})" com o valor de "({vprecomaior})"')
    print('*************************************************************************************************************')
    print()

    return dicprecocatmaior

#Opção 4 - Produto mais barato por categoria

def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    vpreco = 0
    vprecomenor = 0
    vid = ''
    vprod = ''
    vcont = 0
    vcat = categoria
    lstprecocat = []
    dicprecocatmenor = {}
    for i in range(len(dados)):
        vprod = dados[i]['id'] 
        vpreco = dados[i]['preco']
        if vcat == dados[i]['categoria']:
            lstprecocat.append((vprod, float(vpreco)))
            if vpreco > dados[(i+1)]['preco']:
                vid = dados[i]['id'] 
                vprecomenor = dados[i]['preco']
            vcont += 1

    lstvalor = []
    for i in range(len(lstprecocat)):
        lstvalor.append(lstprecocat[i][1])
    lstvalor_ordenada = sorted(lstvalor, reverse=False)
    vprecomenor = lstvalor_ordenada[0]
    for i in range(len(lstprecocat)):
        if vprecomenor == lstprecocat[i][1]:
            vid = lstprecocat[i][0]
            dicprecocatmenor = {'Produto': vid, 'Preço': vprecomenor}
    print()
    print()
    print('*************************************************************************************************************')
    print(f'O dicionário do preço menor por categoria é: \n{dicprecocatmenor}')
    print('*************************************************************************************************************')
    print(f'O produto com menor preço da categoria "({vcat})" é: "\n({vid})" com o valor de "({vprecomenor})"')
    print('*************************************************************************************************************')
    print()
    print()
    
    return dicprecocatmenor


    ...
#Opção 5 - Top 10 produtos mais caros
def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    lstpreco = []
    lstprecoordem = []
    dictop10caro = []
    for i in range(len(dados)):
        lstpreco.append([float(dados[i]['preco']), dados[i]['id']])
        lstprecoordem = sorted(lstpreco, reverse=True)
    for i in range(10):
        dictop10caro.append(lstprecoordem[i])

    print('*********************Relação TOP 10 (10 produtos mais caros)**************************')
    for i in range(len(dictop10caro)):
        print(f'{i+1}º lugar {dictop10caro[i]}')
    print('******************************Fim da relação********************************************')
    return dictop10caro

    ...

#Opção 6 - Top 10 produtos mais baratos
def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    '''
    lstpreco = []
    lstprecoordem = []
    dictop10barato = []
    for i in range(len(dados)):
        lstpreco.append([float(dados[i]['preco']), dados[i]['id']])
        lstprecoordem = sorted(lstpreco, reverse=False)
    for i in range(10):
        dictop10barato.append(lstprecoordem[i])

    print('*********************Relação TOP 10 (10 produtos mais baratos)**************************')
    for i in range(len(dictop10barato)):
        print(f'{i+1}º lugar {dictop10barato[i]}')
    print('******************************Fim da relação********************************************')

    return dictop10barato

def testa_categoria(dados, categoria):
    for i in range(len(dados)):
        if categoria == dados[i]['categoria']:
            return True
            # return dados[i]['categoria']
        else:
            return False
            # print(f'A categoria {categoria} informada não existe!')
            break

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
opcao = 0
while True:
    print('')        
    print('')        
    print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
    print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●Projeto Magalu 1 - Lets Code - 06/02/2022●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
    print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●Controle de Estoque de Produtos - Criado por Walney●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
    print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
    print('                                    1. Listar categorias                                                      ')
    print('                                    2. Listar produtos de uma categoria                                       ')
    print('                                    3. Produto mais caro por categoria                                        ')
    print('                                    4. Produto mais barato por categoria                                      ')
    print('                                    5. Top 10 produtos mais caros                                             ')
    print('                                    6. Top 10 produtos mais baratos                                           ')
    print('                                    0. Sair                                                                   ')
    print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
    opcao = int(input('                                    Escolha uma opção: '))
    print('')        
    print('')        
    if opcao < 0 or opcao > 6 or str(opcao) == '':
        print('Opção inválida! escolha de 0 a 6')
    elif opcao == 1:
        d = obter_dados()
        listar_categorias(d)
    elif opcao == 2:
        d = obter_dados()
        vcat = ''
        vcat = input('Digite uma categoria para listar seus produtos: ')
        listar_por_categoria(d, vcat)
    elif opcao == 3:
        d = obter_dados()
        vcat = ''
        vcat = input('Digite uma categoria para listar o produto mais caro: ')
        if testa_categoria(d, vcat):
            produto_mais_caro(d, vcat)
        else:
            print(f'A categoria {vcat} informada não existe!')
    elif opcao == 4:
        d = obter_dados()
        vcat = ''
        vcat = input('Digite uma categoria para listar o produto mais barato: ')
        if testa_categoria(d, vcat):
            produto_mais_barato(d, vcat)
        else:
            print(f'A categoria {vcat} informada não existe!')
    elif opcao == 5:
        d = obter_dados()
        top_10_caros(d)
    elif opcao == 6:
        d = obter_dados()
        top_10_baratos(d)
    else:

        print('')        
        print('')        
        print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')        
        print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●Programa encerrado pelo usuário!●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
        print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')        
        print('')        
        print('')        
        break



#Programa Principal - não modificar!
d = obter_dados()
menu(d)
