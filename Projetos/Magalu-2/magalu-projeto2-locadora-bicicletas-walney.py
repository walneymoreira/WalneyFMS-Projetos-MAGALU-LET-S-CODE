""" 
*******Arquivo de Classes, métodos, dados e variáveis globais da Locadora de bicicletas********
***PARA EFEITO DE TESTES, OS COMANDOS PARA TESTAR O PROGRAMA, ESTÃO AO FINAL DESTE ARQUIVO******
***É SÓ IR DESMARCANDO OS COMENTÁRIOS EM BLOCO*************************************************
Loja pode: 
•Calcular a conta quando o cliente decidir devolver a bicicleta;
•Mostrar o estoque de bicicletas;
•Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque e modo de aluguel existente.
"""
class Loja:
    def __init__(self): #No método construtor cria uma listas dentro da lista lstclientes com o estoque de bicicletas
        self.lstbicicletas = [
            ['1CCAZ18','Caloi','Cross','Azul','18','','',0,0,0,'n'],
            ['2CPAM22','Caloi','Passeio','Amarela','22','','',0,0,0,'n'],
            ['3CCAM20','Caloi','Cross','Amarelo','20','','',0,0,0,'n'],
            ['4CCAZ18','Caloi','Cross','Azul','18','','',0,0,0,'n'],
            ['5CPAM22','Caloi','Passeio','Amarela','22','','',0,0,0,'n'],
            ['6CCAM20','Caloi','Cross','Amarelo','20','','',0,0,0,'n'],
            ['7CPAZ18','Caloi','Passeio','Azul','18','','',0,0,0,'n'],
            ['8CPRO22','Caloi','Passeio','Roxa','22','','',0,0,0,'n'],
            ['9CCPR22','Caloi','Cross','Preto','22','','',0,0,0,'n'],
        ]
#Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque e modo de aluguel existente.
#Para alugar, passar parâmetros codigo, cliente, tipo_aluguel, qtd_aluguel (ex: loja1.alugar_bicicletas('5CPAM22', cliente2.nome, 'hora', 5))
#Não precisa passar o valor do aluguel que ele calcula.
#NÃO FIZ A CRÍTICA DO CÓDIGO DO CLIENTE PORQUE O PARÂMETRO PASSADO É UM OBJETO CLIENTE JÁ CRIADO, TIPO (cliente1.nome)
# E SE O CODIGO DA BICICLETA EXISTE NO ESTOQUE, PORQUE O ESTOQUE É FIXO E GERADO NA CRIAÇÃO DA LOJA. 
    def alugar_bicicletas(self, codigo, cliente, tipo_aluguel, qtd_aluguel, valor_aluguel=0):
        for listbic in self.lstbicicletas:
            if tipo_aluguel == 'hora':
                valor_aluguel = 5.00
            if tipo_aluguel == 'dia':
                valor_aluguel = 25.00
            if tipo_aluguel == 'semana':
                valor_aluguel = 100.00  
            if listbic[0] == codigo and listbic[10] == 'n':
                listbic[5] = cliente
                listbic[6] = tipo_aluguel
                listbic[7] = qtd_aluguel
                listbic[8] = valor_aluguel
                if qtd_aluguel < 3:
                    listbic[9] = qtd_aluguel*valor_aluguel
                if qtd_aluguel >= 3:
                    listbic[9] = (qtd_aluguel*valor_aluguel) - (qtd_aluguel*valor_aluguel)*(30/100)
                listbic[10] = 's'

#RECEBE A BICICLETA DE VOLTA, CALCULA E INFORMA O VALOR A PAGAR 
#PARÂMETRO A PASSAR É O NOME DO CLIENTE USANDO O OBJETO CLIENTE CRIADO - EXEMPLO (cliente1.nome)
#NÃO FIZ A CRÍTICA SE O CLIENTE EXISTE, PORQUE O NOME PASSADO É DE UM OBJETO CLIENTE JÁ CRIADO
    def devolver_apresentar_conta(self, nome):
        for listbic in self.lstbicicletas:
            if nome in listbic:
                valor_total_a_pagar = listbic[9]
                listbic[5] = ''
                listbic[6] = ''
                listbic[7] = 0
                listbic[8] = 0
                listbic[9] = 0
                listbic[10] = 'n'
        print('********************BICICLETA(S) DEVOLVIDA AO ESTOQUE - VALOR TOTAL A PAGAR***************************')
        print(f'O valor total a pagar, do cliente {nome}, pelo aluguel é: R$ {valor_total_a_pagar}')

#MOSTRA O ESTOQUE DE BICICLETAS TOTAL DO ESTOQUE(ALUGADAS E NÃO ALUGADAS)
    def listar_bicicletas(self):
        print('***************************************LISTAR BICICLETAS DO ESTOQUE***********************************')
        for i in range(len(self.lstbicicletas)):
            print(f'--->Bicicleta {i+1}<-----------------------------------------------------------------------------')
            print(f'Código da bicicleta: {self.lstbicicletas[i][0]}\nMarca da bicicleta: {self.lstbicicletas[i][1]}\nModelo da bicicleta: {self.lstbicicletas[i][2]}\nCor da bicicleta: {self.lstbicicletas[i][3]}\nAro da bicicleta: {self.lstbicicletas[i][4]}\nCliente: {self.lstbicicletas[i][5]}\nTipo de aluguel: {self.lstbicicletas[i][6]}\nQuantidade de aluguel: {self.lstbicicletas[i][7]}\nValor do aluguel===> R$ {self.lstbicicletas[i][8]}\nTotal a pagar===> R$ {self.lstbicicletas[i][9]}\nEstá alugada?: {self.lstbicicletas[i][10]}')
            print('--------------------------------------------------------------------------------------------------')
        print('******************************************************************************************************')

#MOSTRA O ESTOQUE DE BICICLETAS TOTAL DO ESTOQUE(ALUGADAS E NÃO ALUGADAS) DE MANEIRA MAIS SIMPLIFICADA
    def listar_bicicletas_simplificado(self):
        print('***************************************LISTAR BICICLETAS DO ESTOQUE***********************************')
        for i in range(len(self.lstbicicletas)):
            print(f'--->Bicicleta {i+1}<-----------------------------------------------------------------------------')
            print(f'Código: {self.lstbicicletas[i][0]} Marca: {self.lstbicicletas[i][1]} Modelo: {self.lstbicicletas[i][2]} Cor: {self.lstbicicletas[i][3]} Aro: {self.lstbicicletas[i][4]}\nCliente: {self.lstbicicletas[i][5]} Tipo: {self.lstbicicletas[i][6]} Qtd: {self.lstbicicletas[i][7]} Valor: R$ {self.lstbicicletas[i][8]} Total a pagar: R$ {self.lstbicicletas[i][9]} Alugada?: {self.lstbicicletas[i][10]}')
            print('--------------------------------------------------------------------------------------------------')
        print('******************************************************************************************************')

#MOSTRA O ESTOQUE DE BICICLETAS TOTAL DO ESTOQUE(ALUGADAS E NÃO ALUGADAS) POR CÓDIGO INFORMADO NO PARÂMETRO
#PARÂMETROS SÃO O CÓDIGO (ex: '6CCAM20')E A LISTA DO ESTOQUE DA LOJA (ex: loja1.lstbicicletas)
    def listar_bicicletas_por_codigo(self, codigo, lista):
        print(f'****************************DADOS DA BICICLETA {codigo} NO ESTOQUE***********************************')
        vcod = codigo
        for codigo in lista:
            if vcod in codigo:
                print(f'Bicicleta: {codigo}')
        print('******************************************************************************************************')


#MOSTRAR O CADASTRO DOS CLIENTES NA LOJA (ex: loja1.listar_clientes(cliente1.lstclientes))
    def listar_clientes(self, cliente):
        print('***************************************LISTA DO CADASTRO DE CLIENTES***********************************')
        for cliente in cliente:
           print(f'Nome: {cliente[0]:30s} endereço: {cliente[1]:<30s} documento: {cliente[2]:<8s}')
        print('***************************************fim da lista***************************************************')


""" 
Cliente pode: 
•Ver as bicicletas disponíveis na Loja;
•Alugar bicicletas por hora (R$5/hora);
•Alugar bicicletas por dia (R$25/dia);
•Alugar bicicletas por semana (R$100/semana)
•Aluguel para família, uma promoção que 3 ou mais empréstimos (de qualquer tipo) com 30% de desconto no valor total.
OBSERVAÇÃO: 
O método "alugar" por hora, dia, semana e familia, está na classe loja
Entendi que só seria necessário estar na classe cliente, caso no programa que for fazer uso dessas classes
for criado uma modalidade auto-atendimento e portanto, teria um módulo Loja e outro Cliente.
"""

class Cliente:
    lstclientes = []
    def __init__(self, nome, endereco, documento):
        self.nome = nome
        self.endereco = endereco
        self.documento = documento
        self.lstclientes.append([nome, endereco, documento])

#MOSTRAR AS BICICLETAS DISPONÍVEIS NO ESTOQUE DA LOJA PARA ALUGAR
#exemplo: cliente1.mostrar_bicicletas_para_alugar(loja1.lstbicicletas)
    def mostrar_bicicletas_para_alugar(self, loja):
        print('***************************************LISTAR BICICLETAS DO ESTOQUE***********************************')
        for bicicleta in loja:
            if bicicleta[10] == 'n':
                print(f'Código da bicicleta: {bicicleta[0]} marca: {bicicleta[1]} modelo: {bicicleta[2]:<8s} cor: {bicicleta[3]:<8s} aro: {bicicleta[4]}')
        print('***************************************fim da lista***************************************************')

#MOSTRAR AS BICICLETAS QUE SE ENCONTRAM ALUGADAS NO ESTOQUE DA LOJA
#exemplo: cliente1.mostrar_bicicletas_alugadas(loja1.lstbicicletas)
    def mostrar_bicicletas_alugadas(self, loja):
        print('***************************************LISTAR BICICLETAS ALUGADAS*************************************')
        for bicicleta in loja:
            if bicicleta[10] == 's':
                print(f'Código da bicicleta: {bicicleta[0]} marca: {bicicleta[1]} modelo: {bicicleta[2]:<8s} cor: {bicicleta[3]:<8s} aro: {bicicleta[4]}')
        print('***************************************fim da lista***************************************************')

#VER CLIENTES CADASTRADOS (exemplo: cliente1.listar_clientes())
    def listar_clientes(self):
        print('********LISTAR CLIENTES CADASTRADOS*********')
        for i in range(len(self.lstclientes)):
            print(f'=============>  Cliente {i+1}  <==============')
            print(f'Nome do cliente: {self.lstclientes[i][0]:<30s}\nEndereço do cliente: {self.lstclientes[i][1]:<80s}\nDocumento do cliente: {self.lstclientes[i][2]:<15s}')
            print('------------------------------------------')
        print('*******************************************')

'''
龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠
LISTA DAS CLASSES E FUNÇÕES CRIADAS COM SUAS FUNCIONALIDADES E PARÂMETROS:
CLASSE LOJA:
- estoque inicial de bicicletas criado no método construtor da loja.
- método alugar_bicicletas() - Recebe pedidos de aluguéis por hora, diários ou semanais
Para alugar, passar parâmetros codigo, cliente, tipo_aluguel, qtd_aluguel (ex: loja1.alugar_bicicletas('5CPAM22', cliente2.nome, 'hora', 5))
Não precisa passar o valor do aluguel que ele calcula.
- devolver_apresentar_conta() - Recebe a bicicleta de volta e retorna o valor a pagar
Para receber de volta passar o nome do cliente usando o objeto cliente criado. exemplo: devolver_apresentar_conta(cliente1.nome)
- listar_bicicletas() - Lista o estoque total de bicicletas, alugadas e disponíveis na loja. ex: loja1.listar_bicicletas()
- listar_bicicletas_simpificado() - Lista o estoque total de bicicletas, alugadas e disponíveis na loja. ex: loja1.listar_bicicletas_simplificado()
- listar_bicicletas_por_codigo() - Lista pelo código. ex: loja1.listar_bicicletas_por_codigo('8CPRO22', loja1.lstbicicletas)
- listar_clientes - Mostra cadastro de clientes na loja. (ex: loja1.listar_clientes(cliente1.lstclientes))

CLASSE CLIENTE:
- Os clientes são criados e cadastrado pelo método construtor. ex: cliente1 = Cliente('Pedro Carvalho','Rua Sem Fim 546', '88888888')
- mostrar_bicicletas_para_alugar() - Mostra estoque da loja de bicicletas - exemplo: cliente1.mostrar_bicicletas_para_alugar(loja1.lstbicicletas)
- mostrar_bicicletas_alugadas() - Mostra bicicletas alugadas na loja - exemplo: cliente1.mostrar_bicicletas_alugadas(loja1.lstbicicletas)
- listar_clientes() - Ver clientes cadastrados - ex: cliente1.listar_clientes()
龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠

龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠
ABAIXO ESTÃO TODOS OS TESTES FEITOS MARCADOS COMO COMENTÁRIOS - PARA REUTILIZAR É SÓ DESMARCAR COMENTÁRIOS
龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠龠
'''
# from projeto_walney_locadora_bicicletas_classes1 import Loja
# from projeto_walney_locadora_bicicletas_classes1 import Cliente
'''
#**************************************************************************************************************************************
#PARTE 1 - CRIAR LOJAS COM ESTOQUE DE BICICLETAS E CADASTRO DE CLIENTES
#**************************************************************************************************************************************
#Classe Loja
#(1)-Cadastrar/Criar Lojas 
'''
# loja1 = Loja()
# loja2 = Loja()
'''
#**************************************************************************************************************************************
#Classe Cliente
#(2)-Cadastrar/Criar clientes
'''
# cliente1 = Cliente('Pedro Carvalho','Rua Sem Fim 546', '88888888')
# cliente2 = Cliente('José dos Santos e Silva','Rua dos Aflitos 1246', '777777777')
# cliente3 = Cliente('Maria José da Cruz','Rua dos Alagados 675', '999999999')
'''
#**************************************************************************************************************************************
#PARTE 2 - MOSTRAR ESTOQUE DE BICICLETAS E CADASTRO DE CLIENTES
#**************************************************************************************************************************************
#-->Loja1-->cliente - mostrar bicicletas disponiveis para alugar e bicicletas alugadas
'''
# cliente1.mostrar_bicicletas_para_alugar(loja1.lstbicicletas)
# cliente1.mostrar_bicicletas_alugadas(loja1.lstbicicletas)
'''
#-->Loja1 - Listar bicicletas no estoque
'''
# loja1.listar_bicicletas_por_codigo('6CCAM20', loja1.lstbicicletas)
'''
#Loja1 - Listar bicicletas em estoque
'''
# loja1.listar_bicicletas_simplificado()
'''
#-->Loja1 - Listar clientes cadastrados
'''
# loja1.listar_clientes(cliente1.lstclientes)
'''
#-->Loja2-->cliente - mostrar bicicletas disponiveis para alugar e bicicletas alugadas
'''
# cliente1.mostrar_bicicletas_para_alugar(loja2.lstbicicletas)
# cliente1.mostrar_bicicletas_alugadas(loja2.lstbicicletas)
'''
#-->Loja2 - Listar bicicletas no estoque
'''
# loja2.listar_bicicletas_por_codigo('4CCAZ18', loja2.lstbicicletas)
'''
#Loja2 - Listar bicicletas em estoque
'''
# loja2.listar_bicicletas_simplificado()
'''
#-->Loja2 - Listar clientes cadastrados
'''
# loja2.listar_clientes(cliente1.lstclientes)
'''
#**************************************************************************************************************************************
#PARTE 3 - ALUGAR, RECEBER DE VOLTA E APRESENTAR A CONTA DAS BICICLETAS
#**************************************************************************************************************************************
#**************************************************************************************************************************************
#-->loja1 - Alugar bicicleta
'''
# cliente1.mostrar_bicicletas_para_alugar(loja1.lstbicicletas)
# cliente1.mostrar_bicicletas_alugadas(loja1.lstbicicletas)
# loja1.alugar_bicicletas('5CPAM22', cliente2.nome, 'hora', 5, 0)
# loja1.alugar_bicicletas('8CPRO22', cliente3.nome, 'semana', 3, 0)
# loja1.alugar_bicicletas('4CCAZ18', cliente1.nome, 'dia', 2, 0)
# loja1.alugar_bicicletas('6CCAM20', cliente3.nome, 'semana', 1, 0)
# cliente1.mostrar_bicicletas_para_alugar(loja1.lstbicicletas)
# cliente1.mostrar_bicicletas_alugadas(loja1.lstbicicletas)
'''
#-->loja2 - Alugar bicicleta
'''
# #cliente1.mostrar_bicicletas_para_alugar(loja2.lstbicicletas)
# cliente1.mostrar_bicicletas_alugadas(loja2.lstbicicletas)
# loja2.alugar_bicicletas('5CPAM22', cliente2.nome, 'hora', 5, 0)
# loja2.alugar_bicicletas('8CPRO22', cliente3.nome, 'semana', 3, 0)
# loja2.alugar_bicicletas('4CCAZ18', cliente1.nome, 'dia', 2, 0)
# loja2.alugar_bicicletas('6CCAM20', cliente3.nome, 'semana', 1, 0)
# cliente1.mostrar_bicicletas_para_alugar(loja2.lstbicicletas)
# cliente1.mostrar_bicicletas_alugadas(loja2.lstbicicletas)
'''
#************************************************************************************************************************************** 
#-->Loja1-->Cliente - Mostrar dados das bicicletas disponíveis para alugar
'''
# cliente1.mostrar_bicicletas_para_alugar(loja1.lstbicicletas)
# cliente1.mostrar_bicicletas_alugadas(loja1.lstbicicletas)
'''
#-->Loja2-->Cliente - Mostrar dados das bicicletas disponíveis para alugar
'''
# cliente1.mostrar_bicicletas_para_alugar(loja2.lstbicicletas)
# cliente1.mostrar_bicicletas_alugadas(loja2.lstbicicletas)
'''
#**************************************************************************************************************************************
#-->Loja1 - Receber bicicleta de volta e apresentar a conta
'''
# cliente1.mostrar_bicicletas_alugadas(loja1.lstbicicletas)
# cliente1.mostrar_bicicletas_para_alugar(loja1.lstbicicletas)
# loja1.devolver_apresentar_conta(cliente1.nome)
# cliente1.mostrar_bicicletas_alugadas(loja1.lstbicicletas)
# cliente1.mostrar_bicicletas_para_alugar(loja1.lstbicicletas)
#loja1.listar_bicicletas_simplificado()
'''
#-->Loja2 - Receber bicicleta de volta e apresentar a conta
'''
# cliente1.mostrar_bicicletas_alugadas(loja2.lstbicicletas)
# cliente1.mostrar_bicicletas_para_alugar(loja2.lstbicicletas)
# loja2.devolver_apresentar_conta(cliente1.nome)
# cliente1.mostrar_bicicletas_alugadas(loja2.lstbicicletas)
# cliente1.mostrar_bicicletas_para_alugar(loja2.lstbicicletas)
# #loja2.listar_bicicletas_simplificado()
