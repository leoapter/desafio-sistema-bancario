import textwrap                        # Importa a biblioteca textwrap para formatar o texto


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))    # Retorna a opção escolhida pelo usuário


def depositar(saldo, valor, extrato, /):           # Define a função depositar com os parâmetros saldo, valor e extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"  # Adiciona a movimentação de depósito ao extrato, formatando o valor para duas casas decimais
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato                          # Retorna o saldo e o extrato atualizados

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):  # Define a função sacar com os parâmetros saldo, valor, extrato, limite, numero_saques e limite_saques
                                                                            # O parâmetro saldo é obrigatório e os demais são opcionais
                                                                            # Os parâmetros extrato, limite, numero_saques e limite_saques são nomeados
    excedeu_saldo = valor > saldo                         # Verifica se o valor do saque excede o valor do saldo em conta          
    excedeu_limite = valor > limite                       # Verifica se o valor do saque excede o valor limite de saque
    excedeu_saques = numero_saques > limite_saques        # Verifica se o número de saques excede o limite do numero  de saques. Mas não está limitando...!!!. Por que?

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        print(f"\n@@@     O seu saldo disponível é : R$ {saldo:.2f}     @@@")        # Exibe o saldo disponível formatado em Reais e duas casas decimais. 

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor excede o limite de saque. @@@")
        print(f"\n@@@          Limite de saque: R$ {limite:.2f}           @@@")         # Exibe o limite de saque formatado em Reais e duas casas decimais.

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"         # Adiciona a movimentação de saque ao extrato, formatando o valor em Reais e duas casas decimais
        numero_saques += 1                               # Incrementa o número de saques. Não está acrescentando o número de saques. Por que?
        print("\n=== Saque realizado com sucesso! ===")
        print(f"\n===     Número de saques realizados: {numero_saques}     ===")      # Exibe o número de saques realizados
        print(f"\n===     O seu saldo disponível é : R$ {saldo:.2f}     ===")        # Exibe o saldo disponível formatado em Reais e duas casas decimais.

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato                                  # Retorna o saldo e o extrato atualizados


def exibir_extrato(saldo, /, *, extrato):                  # Define a função exibir_extrato com os parâmetros saldo e extrato
                                                           # O parâmetro saldo é obrigatório e o parâmetro extrato é nomeado
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato) # Exibe o extrato se houver movimentações, caso contrário exibe a mensagem "Não foram realizadas movimentações."
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):          # Define a função criar_usuario com o parâmetro usuarios
                                      # O parâmetro usuarios é uma lista de dicionários
    cpf = input("Informe o CPF (somente número): ")  # Solicita ao usuário o CPF. A função input() retorna uma string.
    usuario = filtrar_usuario(cpf, usuarios)         # Chama a função filtrar_usuario passando o CPF e a lista de usuários como argumentos

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})  # Adiciona um novo usuário à lista de usuários

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):     # Define a função filtrar_usuario com os parâmetros cpf e usuarios
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] # Filtra a lista de usuários pelo CPF
    # A lógica Compreetion List acima é equivalente a:
    # Usuarios_filtrados = [] .Cria uma lista vazia para armazenar os usuários filtrados
    # for usuario in usuarios: # Itera sobre a lista de usuários
    #     if usuario["cpf"] == cpf: # Verifica se o CPF do usuário é igual ao CPF informado
    #         usuarios_filtrados.append(usuario) # Adiciona o usuário à lista de usuários filtrados
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):  # Define a função criar_conta com os parâmetros agencia, numero_conta e usuarios. O parâmetro agencia é obrigatório e os demais são opcionais
    cpf = input("Informe o CPF do usuário: ")      # Solicita ao usuário o CPF. A função input() retorna uma string.
    usuario = filtrar_usuario(cpf, usuarios)       # Chama a função filtrar_usuario passando o CPF e a lista de usuários como argumentos

    if usuario:                                    # Verifica se o usuário foi encontrado. Se o usuário foi encontrado, a função filtrar_usuario retorna um dicionário com os dados do usuário
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario} # Retorna um dicionário com os dados da conta
        
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):  # Define a função listar_contas com o parâmetro contas
    for conta in contas:    # Itera sobre a lista de contas
        # Define a variável linha com os dados da conta formatados com a função textwrap.dedent(), que remove a indentação do texto, para facilitar a leitura.
        # Dessa forma, a string pode ser escrita com a indentação que desejar, sem que isso afete a formatação do texto.
        linha = f"""\       
            Agência:\t{conta['agencia']}          
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)                 # Exibe uma linha com 100 caracteres "="
        print(textwrap.dedent(linha))    # Exibe os dados da conta formatados


def main():           # Define a função main
    LIMITE_SAQUES = 3       # Define o limite de saques como 3. Está em letras maiúsculas porque é uma constante
    AGENCIA = "0001"        # Define a agência como "0001" . Está em letras maiúsculas porque é uma constante
    
    saldo = 0               # Define o saldo inicial como zero
    limite = 500            # Define o limite do valor de saque. Está em letras minúsculas porque é uma variável.
    extrato = ""            # Define o extrato como uma string vazia
    numero_saques = 0       # Define o número de saques inicial como zero
    usuarios = []           # Define a lista de usuários como uma lista vazia (a ser preenchida)
    contas = []             # Define a lista de contas como uma lista vazia (a ser preenchida)

    while True:             # Inicia um loop infinito
        opcao = menu()      # Chama a função menu e armazena a opção escolhida pelo usuário

        if opcao == "d":                                            # Verifica se a opção escolhida foi "d"
            valor = float(input("Informe o valor do depósito: "))   # Solicita ao usuário o valor do depósito. A função input() retorna uma string, que é convertida para float.

            saldo, extrato = depositar(saldo, valor, extrato)       # Chama a função depositar passando os parâmetros obrigatórios. 
                                                                    # Esses parâmetros são posicionais porque não possuem um nome. O obrigatórios porque não possuem um valor padrão. 
                                                                    # A função retorna o saldo e o extrato atualizados.

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))  # Solicita ao usuário o valor do saque. A função input() retorna uma string.

            saldo, extrato = sacar(           # Chama a função sacar passando os parâmetros obrigatórios e nomeados. A função retorna o saldo e o extrato atualizados. 
                saldo=saldo,                  # O parâmetro saldo é obrigatório e nomeado
                valor=valor,                  # O parâmetro valor é obrigatório e nomeado
                extrato=extrato,              # O parâmetro extrato é nomeado e opcional
                limite=limite,                # O parâmetro limite é nomeado e opcional
                numero_saques=numero_saques,  # O parâmetro numero_saques é nomeado e opcional
                limite_saques=LIMITE_SAQUES,  # O parâmetro limite_saques é nomeado e opcional
            )

        elif opcao == "e":                            # Verifica se a opção escolhida foi "e"
            exibir_extrato(saldo, extrato=extrato)    # Chama a função exibir_extrato passando o saldo e o extrato como argumentos

        elif opcao == "nu":                           # Verifica se a opção escolhida foi "nu"
            criar_usuario(usuarios)                   # Chama a função criar_usuario passando a lista de usuários como argumento

        elif opcao == "nc":                                         # Verifica se a opção escolhida foi "nc"
            numero_conta = len(contas) + 1                          # Define o número da conta como o tamanho da lista de contas mais 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)    # Chama a função criar_conta passando a agência, o número da conta e a lista de usuários como argumentos.
                                                                    # A lista de usuários é necessária para verificar se o usuário existe antes de criar a conta
                                                                    # A função retorna um dicionário com os dados da conta criada

            if conta:                                               # Verifica se a conta foi criada
                contas.append(conta)                                # Adiciona a conta à lista de contas

        elif opcao == "lc":                                         # Verifica se a opção escolhida foi "lc"
            listar_contas(contas)                                   # Chama a função listar_contas passando a lista de contas como argumento

        elif opcao == "q":                                          # Verifica se a opção escolhida foi "q"
            break                                                   # Encerra o loop

        else:                                                                              # Verifica se a opção escolhida foi inválida
            print("Operação inválida, por favor selecione novamente a operação desejada.") # Exibe uma mensagem de erro caso a opção escolhida seja inválida

main()  # Encerra a execução do programa chamando a função main