#VAR
saldo= 0.0

#FUNÇÕES 
def extrato():
    global saldo

    print('Extrato bancário: ')
    #Listando todos os depósitos 
    for deposito in depositos: 
        print(f'Deposito: R$ {deposito:.2f}')
    #Listando todos os saques
    for saque in saques: 
        print(f'Saque: R$ {saque:.2f}')
    #Calculando e exibindo saldo atual
    print(f'Saldo atual: R$ {saldo:.2f}')
    #Se não houver movimentações, exiba uma mensagem
    if not depositos and not saques: 
        print('Nao foram realizadas movimentações')
#Criando listas para registrar depositos e saques 
depositos = []
saques = []

saldo = 0.0
#--------------------------------------------------------------------------------
def depositar (valor):
    global saldo #Essa palavra global ta sendo usada pra localizar a variavel saldo

    #Verificando se o valor é positivo 
    if valor > 0:
        saldo += valor
        print(f"Deposito de {valor:.2f} realizado com sucesso")
    else: 
        print("O valor deverá ser maior que zero ")
        
#--------------------------------------------------------------------------------

def sacar(valor):
    global saldo
    
    if valor <= saldo:
        if valor <= 500:
            saldo -= valor 
            print (f'Saque de R$ {valor:.2f} realizado com sucesso ')
        else: 
            print('O Valor de saque exce o limite diário do usuário')
    else: 
        print('Saldo insuficiente para o saque ')

#--------------------------------------------------------------------------------

valor_deposito = float(input('Digite o valor que deseja realizar o depósito: '))
depositar(valor_deposito)

valor_saque = float(input('Digite o valor do saque: '))
sacar(valor_saque)

extrato()

