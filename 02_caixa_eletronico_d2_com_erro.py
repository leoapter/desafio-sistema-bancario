import textwrap   # Importa a biblioteca textwrap para formatação de texto

def menu():                                              
    menu = """\n                                         
    ================= CAIXA ELETRÔNICO =================
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Cadastrar Nova Conta
    [nu]\t Cadastrar Novo Usuário
    [lc]\t Listar Contas
    [q]\t Sair
    => """                                                
    
    return input(textwrap.dedent(menu))           # Retorna a opção escolhida pelo usuário


def depositar(saldo, valor, extrato, /):          # Função depositar. O simbolo "/" impõe que os argumentos sejam passados por posição. 
    if valor > 0:                                 # Se o   valor for maior que zero
        saldo += valor                            # Soma o valor do depósito ao saldo
        extrato += f"Depósito: R$ {valor:.2f}\n"  # Acrescenta no extrato o valor do depósito formatado em 2 casas decimais e pula uma linha
        print("Depósito realizado com sucesso!")  # Emite aviso de sucesso
    else:
        print("@@@Operação falhou! O valor informado é inválido.@@@") # Emite aviso de erro

    return saldo, extrato                         # Retorna o saldo e o extrato

def sacar(*, saldo, valor, extrato, limite_do_saque, numero_saques, limite_de_saques):  # Função sacar. O simbolo "*" impõe que os argumentos sejam passados por nome 
    excedeu_saldo = valor > saldo                    # Compara o valor do saque com o saldo em conta corrente
    excedeu_limite = valor > limite_do_saque                  # Compara o valor do saque com o limite de saque
    excedeu_saques = numero_saques > limite_de_saques  # Compara o numero de saques com a quantidade máxima de saques

    if excedeu_saldo:  # Se o valor do saque excede o saldo
        print("\n@@@ Operação falhou! Você não tem saldo suficiente.@@@")  # Emite aviso de erro

    elif excedeu_limite:  # Se o valor do saque excede o limite
        print("\n@@@ Operação falhou! O valor do saque excede o limite.@@@")  # Emite aviso de erro

    elif excedeu_saques:  # Se o numero de saques excede o limite diário
        print("\n@@@ Operação falhou! Número máximo de saques excedido.@@@")  # Emite aviso de erro

    elif valor > 0:                            # Se o valor do saque é positivo
        saldo -= valor                         # Subtrai do saldo o valor do saque
        extrato += f"Saque: R$ {valor:.2f}\n"  # Acrescenta no extrato o valor do saque formatado em 2 casas decimais e pula uma linha
        numero_saques += 1                     # Atualiza o contador de saques
        print("\n=== Saque realizado com sucesso!===")  # Emite aviso de sucesso

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido.@@@")  # Emite aviso de erro

    return saldo, extrato  # Retorna o saldo e o extrato

def extrato(saldo, /, *, extrato):  # Função extrato. O simbolo "/" impõe que os argumentos sejam passados por posição e o "*" impõe que os argumentos sejam passados por nome
    print("\n================ EXTRATO ================")  # Imprime o cabeçalho do extrato
    print("Não foram realizadas movimentações." if not extrato else extrato)  # Imprime o extrato se houver movimentações, senão imprime a mensagem de extrato vazio
    print(f"\nSaldo: R$ {saldo:.2f}")                    # Imprime o saldo formatado em 2 casas decimais
    print("==========================================")  # Imprime o rodapé do extrato

def cadastrar_usuario(usuarios, /):  # Função cadastrar_usuario. O simbolo "/" impõe que os argumentos sejam passados por posição
    cpf = input("Informe o CPF (somente números): ") ### Solicita o CPF do usuário antes de prosseguir com o cadastro de novo usuário
    usuario = filtrar_usuario(cpf, usuarios)  # Filtra o usuário pelo CPF informado

    if usuario:
        print("@@@ CPF já cadastrado. Tente novamente. @@@")  # Emite aviso de CPF já cadastrado
    
    else:
        usuarios.append(cpf)  # Adiciona o CPF na lista de usuários
        print("=== Usuário cadastrado com sucesso! ===")  # Emite aviso de sucesso no cadastro

    nome = input("Informe o nome completo: ")  # Solicita o nome do usuário
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")  # Solicita a data de nascimento do usuário
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")  # Solicita o endereço do usuário

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

def listar_contas(contas):
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
    limite_do_saque = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite_do_saque,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()

def main():  # Função principal
    LIMITE_DE_SAQUES = 3   # Variavel global. Quantidade máxima de saques diários        
    AGENCIA = "0001"       # Variavel global

    saldo = 0                 # Saldo inicial ZERO
    extrato = ""              # Extrato inicial VAZIO
    limite_do_saque = 500     # Valor limite de saque por transação
    numero_saques = 0         # Contador de saques
    usuarios = []             # Lista de usuários
    contas = []               # Lista de contas
    
    while True:               # Loop infinito
        opcao = menu()

        if opcao == "d":  # Se a opção escolhida é d, inicia aqui
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":  # Se a opção escolhida é s, inicia aqui
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite_do_saque=limite_do_saque, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_DE_SAQUES
                )

        elif opcao == "e":  # Se a opção escolhida é e, inicia aqui
            extrato(saldo, extrato=extrato)

        elif opcao == "nc":  # Se a opção escolhida é nc, inicia aqui
            criar_conta(AGENCIA, 1, usuarios)

        elif opcao == "nu":  # Se a opção escolhida é nu, inicia aqui
            cadastrar_usuario(usuarios)

        elif opcao == "lc":  # Se a opção escolhida é lc, inicia aqui
            listar_contas(contas)

        elif opcao == "q":  # Se a opção escolhida é q, inicia aqui
            print("Obrigado por utilizar nossos serviços!!! \n")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

(main)           