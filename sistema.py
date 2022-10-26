global conta
conta = []
def criar_conta(*args):
    contas = True
    while contas:
        numero_conta = int(input("Informe um número para a conta:\n"))
        titular_conta = str(input("Informe seu nome:\n"))
        saldo_conta = float(input("Informe um valor para o seu primeiro depósito:\n"))
        senha_conta = str(input("Crie uma senha:\n"))
        contas = str(input("Deseja criar outra conta?\n Digite S para sim ou N para não\n"))
        if contas =='s':
            contas = True
        elif contas == 'n':
            contas = False
        conta_cadastrada = {
            'numero' : numero_conta,
            'titular' : titular_conta.title(),
            'saldo' : saldo_conta,
            'senha' : senha_conta
        }
        conta.append(conta_cadastrada)

def acessar_conta(conta):
    global minha_conta
    numero = int(input("Informe o número da conta:\n"))
    senha = str(input("Informe a senha da conta:\n"))
    while numero == '' or senha == '':
        menu()
    for minha_conta in conta:
        if minha_conta['numero'] == numero and minha_conta['senha'] == senha:
            print("\n")
            print("Olá,", minha_conta['titular'])
            print("R$", minha_conta['saldo'], '\n')
            menu_conta()
            return minha_conta
    print("Conta não encontrada!\nVerifique se os dados estão corretos\n")


def remover_conta():
    conta.remove(minha_conta)
    print("Conta Apagada!\n")
    menu()

def transferencia():
    conta_transferencia = int(input("Informe a conta destino\n"))
    for conta_cliente in conta:
        if conta_cliente['numero'] != conta_transferencia or conta_transferencia == minha_conta['numero']:
            print("Conta Inválida!\n Verifique se os dados estão corretos\n")
            menu_conta()
        else:
            valor_transferencia = float(input("Informe o valor da transferência\n"))
            if valor_transferencia < 0.0 or valor_transferencia > minha_conta['saldo']:
                print("Saldo Insuficiente!\n")
                menu_conta()
            else:
                minha_conta['saldo'] -= valor_transferencia
                conta_cliente['saldo'] += valor_transferencia

def mostra_saldo():
    saldo = minha_conta['saldo']
    print("R$",saldo)
    menu_conta()

def depositar():
    conta_deposito = int(input("Informe o Número da Conta Destino\n"))
    for conta_cliente in conta:
        if conta_cliente['numero'] == conta_deposito:
            valor_deposito = float(input("Informe o Valor do Depósito\n"))
            conta_cliente['saldo'] += valor_deposito
            print("Depósito Realizado com Sucesso!\n")
            menu_conta()
    print("Conta não encontrada!\nVerifique se os dados estão corretos\n")


def mostra_contas(conta):
    print(conta)
    menu()

def menu():
    menu = True
    while menu:
        print("""
        1 - Crie uma Conta agora mesmo
        2 - Acessar uma conta
        3 - Mostrar Contas
        """)
        op = input("Escolha uma opção:\n")
        while op == ' ':
            op = input("Escolha uma opção:\n")
        if op == '1':
            print("Vamos começar a criar sua conta")
            criar_conta()
        elif op == '2':
            acessar_conta(conta)
        elif op == '3':
            mostra_contas(conta)

def menu_conta():
    menu2 = True
    while  menu2:
        print("""
        1 - Remover Conta
        2 - Realizar Transferência
        3 - Exibir Saldo
        4 - Fazer Depósito
        5 - Voltar ao Menu Anterior
        6 - Mostra Contas
        """)

        op = input("Escolha uma opção:\n")
        while op == ' ':
            op = input("Escolha uma opção:\n")
        if op == '1':
            print("===== Remover Conta =====")
            remover_conta()
        elif op == '2':
            print("===== Realizar uma Transferência =====")
            transferencia()
        elif op == '3':
            print("===== Saldo =====")
            mostra_saldo()
        elif op == '4':
            print("===== Fazer Depósito =====")
            depositar()
        elif op == '5':
            menu()
        elif op == '6':
            mostra_contas(conta)

menu()
