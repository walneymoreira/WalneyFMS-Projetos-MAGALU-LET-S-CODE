#***********************************************************************************************************************************
# Let's Code - Magalu - Projeto 3 - ESTRUTURA DE DADOS - 16/02/2022 - Walney Francisco Moreira de Sousa - Professores: Brain e Paulo
#***********************************************************************************************************************************
## Projeto Módulo 3
#***********************************************************************************************************************************
# Você irá receber uma lista bi-dimensional com altura e largura não necessáriamente iguais contendo apenas 
# 0's e 1's. Cada 1 representa um pedaço de rio, enquanto os 0's representam terra. Rios são compostos por 
# 1's adjacentes horizontalmente ou verticalmente (mas não diagonalmente). O número de 1's adjacentes representa
#  o tamanho do rio.
# Note que o rio pode fazer curvas, isto é, rios podem ter formato de L ou até mesmo de cruz e são considerados 
# um rio só.
# Crie um algoritmo que receba esta lista bi-dimensional e retorne uma lista com os tamanhos dos rios dentro 
# dessa estrutura, os tamanhos de rios dentro da lista resposta não precisam ter uma ordem específica.
# **Exemplo de entrada:**
# python
# matrix = [
#     [1, 0, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 0],
# ]

# **Saída esperada:**
# python
# [1, 2, 2, 2, 5] # Note que os números poderiam estar em qualquer ordem dentro da lista
# podemos visualizar os rios claramente na seguinte estrutura:
# python
# [1,  ,  , 1,  ]
# [1,  , 1,  ,  ]
# [ ,  , 1,  , 1]
# [1,  , 1,  , 1]
# [1,  , 1, 1,  ]
#***********************************************************************************************************************************
#***********************************************************************************************************************************
# Let's Code - Magalu - Projeto 3 - ESTRUTURA DE DADOS - 16/02/2022 - Walney Francisco Moreira de Sousa Professores: Brain e Paulo
#***********************************************************************************************************************************
## Projeto Módulo 3
#***********************************************************************************************************************************
def encontrarios(matriz, linha, coluna):
    vtam = 1
    if linha+1 < len(matriz) and matriz[linha+1][coluna] == 1:
        matriz[linha+1][coluna] = '-1'
        vtam += encontrarios(matriz, linha+1, coluna)
    if linha-1 >= 0 and matriz[linha-1][coluna] == 1:
        matriz[linha-1][coluna] = '-1'
        vtam += encontrarios(matriz, linha-1, coluna)
    if coluna+1 < len(matriz[linha]) and matriz[linha][coluna+1] == 1:
        matriz[linha][coluna+1] = '-1'
        vtam += encontrarios(matriz, linha, coluna+1)
    if coluna-1 >=0 and matriz[linha][coluna-1] == 1:
        matriz[linha][coluna-1] = '-1'
        vtam += encontrarios(matriz, linha, coluna-1)
    return vtam

def qtdrios(matriz):
    lsttamanhorios = []
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == 1:
                matriz[linha][coluna] = '-1'
                lsttamanhorios.append(encontrarios(matriz, linha, coluna))                  
    return lsttamanhorios

#Matriz para teste
# matrix = [
#         [0, 0, 0, 1, 1],
#         [0, 1, 1, 0, 1],
#         [0, 1, 1, 0, 1],
#         [1, 0, 1, 0, 1],
#         [1, 0, 1, 1, 1]
#         ]

#Matriz para teste
# matrix = [
#         [0, 1, 0, 1, 0],
#         [1, 1, 1, 1, 1],
#         [0, 1, 0, 1, 0],
#         [1, 1, 1, 1, 1],
#         [0, 1, 0, 1, 0]
#         ]

#Matriz para teste
# matrix = [
#         [1, 1, 0, 0, 1],
#         [0, 1, 0, 1, 0],
#         [0, 0, 1, 1, 0],
#         [0, 1, 0, 1, 0],
#         [1, 0, 0, 0, 1]
#         ]

matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
        ]


matriz_final = sorted(qtdrios(matrix))
print('****Lista dos rios e seus tamanhos encontrados*****')
for i in range(len(matriz_final)):
    print(f'Tamanho do rio {i+1} --> {matriz_final[i]}')
print('***************************************************')
print(f'Lista dos rios encontrados---> {matriz_final}')
print('***************************************************')

