from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:        
        def __init__(self, endereco ):
            self.endereco = endereco
            self.contas = []

        def realizar_transacao(self, conta, transacao): # Módulo realizar_transacao
            self.conta()
            self.transacao

        def adicionar_conta(self):                      # Módulo adicionar_conta
            self.conta()

class PessoasFisica(Cliente):         
        def __init__(self, cpf, nome, data_nascimento, endereco):
            super().__init__(endereco)
            cpf = cpf
            nome = nome
            data_nascimento = data_nascimento

class Conta:
    def __init__(self):
        pass

class ContaCorrente(Conta):           
        def __init__(self):
        super().__init__()

class Historico:
    def __init__(self):
        pass

# Classes Abstratas
# Interfaces são contratos que definem o que uma classe deve fazer ou não.
# Interfaces são classes abstratas que definem métodos que devem ser implementados por suas subclasses.
# Em Python, uma classe abstrata é uma classe que não pode ser instanciada, mas pode ser herdada.
# Quando transformamos um método em abstrato, transformamos a classe em abstrata.
# Uma classe abstrata é uma classe que contém pelo menos um método abstrato.
# Logo, transformando a classe em classe abstrata, estamos dizendo que ela não poderé mais ser instanciada, mas poderá ser herdada por outras classes.
# Para criar uma classe abstrata em Python, você deve importar o módulo ABC e o decorador abstractmethod do pacote abc.
# O decorador abstractmethod é usado para definir um método abstrato em uma classe abstrata.
# Uma classe abstrata é uma classe que contém pelo menos um método abstrato.

# Contrato de uma classe abstrata:
# - A classe abstrata deve ser herdada por outras classes.
# - A classe abstrata não pode ser instanciada.
# - A classe abstrata deve conter pelo menos um método abstrato.
# - O método abstrato deve ser implementado por suas subclasses.
# - A classe abstrata pode conter métodos concretos.
# - A classe abstrata pode conter propriedades abstratas.
# - A propriedade abstrata deve ser implementada por suas subclasses.
# - A classe abstrata pode conter propriedades concretas.
# - A propriedade concreta não precisa ser implementada por suas subclasses.

# Sintaxe:
# from abc import ABC, abstractmethod
# class NomeDaClasse(ABC):
#     @abstractmethod
#     def nome_do_metodo(self):
#         pass

class Transacao(ABC):     # Criando uma classe abstrata
     @property
     @abstractclassmethod
     def valor(self):
          pass
     
     @abstractclassmethod
     def registrar(self, conta):
          pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor