import textwrap


## 07:12 VÍDEO

def menu():
    menu = """
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nc] Nova conta
    [nu] Novo usuário
    [lc] Listar Contas
    [q]  Sair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n DEPOSITO REALIZADO COM SUCESSO")
    else:
        print("DEPOSITO FALHOU, FORMATO INVÁLIDO")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n operação falhou, saldo insuficiente")

    elif excedeu_limite:
        print("\n operação falhou, saque excede o limite")

    elif excedeu_saques:
        print("\n operação falhou, numero máximo de saques excedido")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso")

    else:
        print("\n OPERAÇÃO FALHOU, VALOR INFORMADO INVÁLIDO")


def exibir_extrato(saldo, /, *, extrato):
    print('\n================EXTRATO================')
    print('NÃO FORAM REALIZADAS TRANSAÇÕES' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('\n=======================================')


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe um usuário com esse CPF!')
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (rua, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print('USUÁRIO CRIADO!')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuarios["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o cpf do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nCONTA CRIADA COM SUCESSO")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("USUÁRIO NÃO ENCONTRADO, FLUXO DE CRIAÇÃO DE CONTA ENCERRADO")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input("Informe o valor a sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break


main()