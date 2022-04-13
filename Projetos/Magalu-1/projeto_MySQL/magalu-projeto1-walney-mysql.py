import json
import os.path
import sys
import operator
from datetime import date
import mysql.connector
#from processa import obter_dados, menu
con = mysql.connector.connect(host='localhost',database='bd_projeto1',user='root',password='_Wfms1959_')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)

#Opção 1 - Listar categorias 
def listar_categorias():
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    sql = ("SELECT categoria 'Categoria de produtos', count(categoria) 'Quantidades de produtos desta categoria' FROM dados GROUP BY categoria")
#    sql = ('SELECT categoria FROM dados GROUP BY categoria ORDER BY categoria')
    cursor.execute(sql)
    numrows = int(cursor.rowcount)
    print('------------------------------------------------------------------------')
    print('-------Lista das categorias cadastradas---------------------------------')
    print('| Categorias      Quantidade de produtos                               |')
    print('------------------------------------------------------------------------')
    a = 0
    for row in cursor.fetchall():
        a += 1
        print(row[0], '---------->', row[1])
    print('Quantidade de categorias: ', a)
    print('------------------------------------------------------------------------')

#Opção 2 - Listar produto de uma categoria
def listar_por_categoria(vcat):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    vstr = "SELECT categoria, id, preco FROM dados WHERE categoria = '" + vcat + "' ORDER BY categoria, id;"
    print(vstr)
    sql = (vstr)
    cursor.execute(sql)
    numrows = int(cursor.rowcount)
    print('------------------------------------------------------------------------')
    print('-------Lista de produtos da categoria ', vcat, '-----------------------------')
    print('| Categoria                             ID        Preço                |')
    print('------------------------------------------------------------------------')
    a = 0
    for row in cursor.fetchall():
        a += 1
        print(' ',row[0],' ',row[1], ' ',row[2])
    print('Quantidade de produtos da categoria: ', a)
    print('------------------------------------------------------------------------')

#Opção 3 - Produto mais caro por categoria
def produto_mais_caro(vcat):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    vstr = "SELECT categoria 'Categoria de produtos', id 'Produto', MIN(CAST(preco AS DECIMAL(10,2)))'Preço' FROM dados WHERE categoria = '" + vcat +"'GROUP BY categoria ORDER BY preco;"
    print(vstr)
    sql = (vstr)
    cursor.execute(sql)
    numrows = int(cursor.rowcount)
    print('------------------------------------------------------------------------')
    print('-------Lista do produto mais barato da categoria ', vcat, '-----------------------------')
    print('| Categoria                             ID        Preço                |')
    print('------------------------------------------------------------------------')
    a = 0
    for row in cursor.fetchall():
        a += 1
        print(' ',row[0],' ',row[1], ' ',row[2])
#    print('Quantidade de produtos da categoria: ', a)
    print('------------------------------------------------------------------------')

#Opção 4 - Produto mais barato por categoria

def produto_mais_barato(vcat):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    vstr = "SELECT categoria 'Categoria de produtos', id 'Produto', MAX(CAST(preco AS DECIMAL(10,2)))'Preço' FROM dados WHERE categoria = '" + vcat +"'GROUP BY categoria ORDER BY preco;"
    print(vstr)
    sql = (vstr)
    cursor.execute(sql)
    numrows = int(cursor.rowcount)
    print('------------------------------------------------------------------------')
    print('-------Lista do produto mais caro da categoria ', vcat, '-----------------------------')
    print('| Categoria                             ID        Preço                |')
    print('------------------------------------------------------------------------')
    a = 0
    for row in cursor.fetchall():
        a += 1
        print(' ',row[0],' ',row[1], ' ',row[2])
#    print('Quantidade de produtos da categoria: ', a)
    print('------------------------------------------------------------------------')


#Opção 5 - Top 10 produtos mais caros
def top_10_caros():
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''

#Opção 6 - Top 10 produtos mais baratos
def top_10_baratos():
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    '''

def menu():
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
        print('                                    3. Produto mais barato por categoria                                        ')
        print('                                    4. Produto mais caro por categoria                                      ')
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
            listar_categorias()
        elif opcao == 2:
            vcat = ''
            vcat = input('Digite uma categoria para listar seus produtos: ')
            listar_por_categoria(vcat)
        elif opcao == 3:
            vcat = ''
            vcat = input('Digite uma categoria para listar o produto mais barato: ')
            produto_mais_caro(vcat)
        elif opcao == 4:
            vcat = ''
            vcat = input('Digite uma categoria para listar o produto mais caro: ')
            produto_mais_barato(vcat)
        elif opcao == 5:
            top_10_caros()
        elif opcao == 6:
            top_10_baratos()
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

menu()
