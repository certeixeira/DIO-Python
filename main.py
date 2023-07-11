menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor_sacado = 0

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Foi depositado R${valor:.2f}\n"

        else:
            print("Valor a depositar é inválido, operação cancelada!")

    elif opcao == "s":
        valor = float(input("Digite o valor a sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou, você não tem saldo o suficiente")

        elif excedeu_limite:
            print("Operação falhou, o valor do saque excede o limite")

        elif excedeu_saques:
            print("Operação falhou, número máximo de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Foi sacado R${valor:.2f}\n"
            numero_saques += 1
            valor_sacado += valor

        else:
            print("Operação falhou, valor informado é inválido")

    elif opcao == "e":
        print("\n.......... EXTRATO ..........")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print(f"Total sacado: R${valor_sacado:.2f}")
        print("...............................")

    elif opcao == "q":
        print("OPERAÇÃO CANCELADA")
        break

    else:
        print("Operação inválida, selecione novamente a opção desejada")


