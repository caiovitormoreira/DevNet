# class é como uma receita de bloco. Será a receita do objeto: Ingredientes e modo de preparo

class ContaCorrente:

    def __init__(self, numero_cc, titular, saldo, limite):
        print("Contruindo um objeto ... {}".format(self))
        self.__numero_cc = numero_cc
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_numero_cc(self):
        return (self.__numero_cc)
    def get_titular(self):
        return (self.__titular)
    def get_saldo(self):
        return (self.__saldo)
    def get_limite(self):
        return (self.__limite)

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def extrato(self):
        print("Saldo do titular {} é de {}".format(self.__titular, self.__saldo))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        print("Transferido {} de {} para {}".format(valor, self.__titular, destino.__titular))
        print("Conta {} de {} tem extrato de {}".format(self.get_numero_cc(), self.get_titular(), self.__saldo))
        print("Conta {} de {} tem extrato de {}".format(destino.__numero_cc, destino.__titular, destino.__saldo))

    def set_limite(self, novo_limite):
        self.__limite = novo_limite
