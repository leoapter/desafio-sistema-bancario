# Inicio da String. As 3 " permitem quebrar a linha dentro do texto

menu = """

================= CAIXA ELETRÔNICO =================
Escolha uma das opções abaixo:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
____________________________________________________


=> """       # Aqui as 3" finalizam a Sring

saldo_conta_corrente = 0  # Saldo inicial ZERO
extrato = ""              # Extrato inicial VAZIO. Recebe o valor da variável extrato em todas as opções

# Condições Gerais do Desafio
limite_saque = 500
numero_saques = 0
LIMITE_SAQUES_DIARIO = 3

while True:   # Causa Loop Infinito a não ser que interrompido (elif q)

    opcao = input(menu)  # Insere aqui a opção escolhida no menu

    if opcao == "d":  # Se a opção escolhida é d, inicia nesse if
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:        # Se o valor do deposito é positivo
            saldo_conta_corrente += valor   # Acrescenta o valor ao saldo existente
            extrato += f"Depósito: R$ {valor:.2f}\n" # F String, Acrescenta no extrato o valor do depósito formatado em 2 casas decimais e pula uma linha

        else:
            print("Operação falhou! O valor informado é inválido.")  # Caso contrário, emite aviso de erro

    elif opcao == "s":  # Se a opção escolhida é s, inicia nesse if
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo_conta_corrente # Compara o valor do saque com o saldo em conta corrente 

        excedeu_limite = valor > limite_saque # Compara o valor do saque com o limite de saque

        excedeu_saques = numero_saques >= LIMITE_SAQUES_DIARIO # Compara o numero de saques com a quantidade máxima de saques

        if excedeu_saldo:
            print(f"Você não tem saldo suficiente. Saldo Disponível R$ {saldo_conta_corrente:.2f}")

        elif excedeu_limite:
            print(f"O valor do saque excede o limite máximo de R$ {limite_saque:.2f} .")

        elif excedeu_saques:
            print(f"Número máximo de saques excedido: {LIMITE_SAQUES_DIARIO}")

        elif valor > 0:  # Essa comparação impede o saque de valor negativo
            saldo_conta_corrente -= valor  # subtrai do saldo, o valor do saque 
            extrato += f"Saque: R$ {valor:.2f}\n"  # 
            numero_saques += 1  #Atualiza o contador de saques 

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo_conta_corrente:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços!!! \n")
        print()
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")