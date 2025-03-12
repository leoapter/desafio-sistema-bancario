# Desafio Sistema Bancário
## Desfio 1
Nesta primeira etapa vamos simular um sistema de caixa eletrônico
### Requisitos
- 1- Três Operações: Depósito, Saque e Extrato. 
- 2- Depósitos: Aceitar apenas depósitos positivos, de qualquer valor. 
- 3- Saques: Permitir no máximo 3 saques diários, de no máximo R$ 500,00, 
- 4- Extrato: Listar todos os Depósitos e Saques. Valores exibidos no formato R$ xxx.xx
  

## Desfio 2
Nesta segunda etapa vamos melhorar o sistema de caixa eletrônico do Desafio 1
### Requisitos
- 1- Transformar as opções existentes (depósito, saque e extratos) em funções
- 2- Criar 2 novas funções: 
-   2.1 - Cadastrar usuário(novo cliente):
    Nome, data de nascimento, CPF(somente números), endereço (logradouro, numero - bairro - cidade/sigla estado).
    Não pode haver 2 usuários com o mesmo CPF.
-   2.2- Cadastrar conta bancária (vinculada ao usuário):
    O programa deve armazenarcontas em uma lista compoesta por:
    Agencia, numero da conta e usuário.
    O numero da conta é sequencial, iniciando em 1.
    O numero da agência é fixo:"0001".
    O usuário pode ter mais de uma conta.
    O conta pode ter apenas um usuário.
    DICA:Para vincular um um usuário à uma conta, filtre a lista de usuários buscando o CPF na lista.
- 3- Criar funções para todas as opções.
- 4- Cada função terá uma regra na passagem de argumentos.
- 5- O retorno e a forma como serão chamadas ficam a nosso critério.
- 6- A função saque deve receber os argumentos apenas por nome(keyword only):
     Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
     Sugestão de retorno: saldo e extrato.
- 7- A função depósito deve receber os argumento apenas por posição (positional only):
     Sugestão de argumentos: saldo, valor, extrato.
     Sugestão de retorno: saldo, extrato.
- 8- A função extrato deve receber os argumentos por posição e nome (positional only e keyword only):
     Argumentos posicionais: saldo. Argumentos nomeados: extrato
- 9- Pode criar novas funções, por exemplo: listar contas, listar usuários, inativar contatodos os Depósitos e Saques. Valores exibidos no formato R$ xxx.xx
