# class é como uma receita de bloco. Será a receita do objeto: Ingredientes e modo de preparo

class ContaCorrente:

    def __init__(self, numero_cc, titular, saldo, limite):
        print("Contruindo um objeto ... {}".format(self))
        self.__numero_cc = numero_cc
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero_cc(self):
        print("chamado o get numero_cc, mas com @properties")
        return (self.__numero_cc)

    @property
    def titular(self):
        print("chamado o get titular, mas com @properties")
        return (self.__titular.title())
        #esse title() faz a primeira letra ficar maíuscula
    @property
    def saldo(self):
        print("chamado o get saldo, mas com @properties")
        return (self.__saldo)


    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_disponivel >= valor_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Error 304: you're broke!")

    def extrato(self):
        print("Saldo do titular {} é de {}".format(self.__titular, self.__saldo))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        print("Transferido {} de {} para {}".format(valor, self.__titular, destino.__titular))
        print("Conta {} de {} tem extrato de {}".format(self.get_numero_cc(), self.get_titular(), self.__saldo))
        print("Conta {} de {} tem extrato de {}".format(destino.__numero_cc, destino.__titular, destino.__saldo))

    @property
    def limite(self):
        print("chamado o metodo de get.limite, mas com @properties")
        return (self.__limite)

    @limite.setter
    def limite(self, novo_limite):
        print("chamado o metodo de set limite, mas com @setter")
        self.__limite = novo_limite

    @staticmethod #static methods pertencem a classe. Isso significa que nao precisa de um objeto criado para chamar esse metodo
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
