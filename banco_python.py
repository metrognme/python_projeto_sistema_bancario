import textwrap

def menu():
    menu_texto = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo Usuário
    [nc]\tNova Conta
    [lc]\tListar Contas
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_texto)).lower()

def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito:\tR$ {valor:.2f}")
            print("\n=== Depósito realizado com sucesso! ===")
            print(f'=== Seu saldo atual é de R${saldo:.2f} ===')
        else:
            print("\nOperação falhou! O valor informado é inválido.")
    except ValueError:
        print("\nOperação falhou! Digite apenas números.")

    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
        return saldo, extrato, numero_saques
    
    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        print("\nOperação falhou! Digite apenas números.")
        return saldo, extrato, numero_saques

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")


    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque:\t\tR$ {valor:.2f}")
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
        print(f'=== Seu saldo atual é de R${saldo:.2f} ===')

    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in extrato:
            print(transacao)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nErro! Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print(f'=== Usuário {nome} criado com sucesso! ===')

def filtrar_usuario(cpf, usuarios):
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                return usuario
        return None

def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}

    print("\nErro! Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    if not contas:
        print("\n=== Não existem contas cadastradas! ===")
        return
        
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("Saindo...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()