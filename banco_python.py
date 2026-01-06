# SISTEMA DO BANCO PYTHON

menu = """
[d] depositar
[s] sacar
[e] extrato
[q] sair
""".lower()

saldo = 0
limite = 500
extrato = []
numero_saques = 0
limites_saques = 3

while True:
    opcao = input(menu)

    if opcao == "q":
        break
    elif opcao == "d":
        try:
            deposito = float(input("Quanto gostaria de depositar?"))
        except ValueError:
            print("Digite um valores númericos apenas!")
            continue
        saldo += deposito
        extrato.append(f'Depósito: +R${deposito:.2f}')
        print(f'Seu saldo pós depósito é de R${saldo:.2f}')
    elif opcao == "s":
        if limites_saques > 0:
            print(f'Seu saldo atual é R${saldo:.2f}. \nLemrando que só são permitidos até {limites_saques} saques diários e lhe restam {limites_saques - numero_saques} saques para o dia de hoje.')
        else:
            print("Limite de saques atingido. Você não pode mais realizar saques no dia de hoje!")
            continue
        try:
            saque = float(input("Que valor deseja sacar?"))
        except ValueError:
            print("Digite um valores númericos apenas!")
            continue
        if saque <= saldo and saque <= limite:
            saldo -= saque
            limite -= saque
            limites_saques -= 1
            extrato.append(f'Saque: -R${saque:.2f}')
            print(f'Seu saldo pós saque é de R${saldo:.2f}.')
        else:
            print(f'O valor solicitado excede seu saldo ou o limite diário de saques.')
            continue
    elif opcao == "e":
        print("<======================EXTRATO======================>")
        if not extrato:
            print("Sem extrato até o momento.")
        else:
            historico = "\n".join(extrato)
            print(historico)
            print(f'\nSaldo: R${saldo:.2f}')
        print("<======================EXTRATO======================>")
    else:
        continue

