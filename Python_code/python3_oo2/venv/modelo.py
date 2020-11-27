class Programa: #essa agora é uma classe mae. As outras classes vão herdar os atributos e os metodos
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def likes_increase(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self):
        return self.__nome

class Filme(Programa): #passando o nome da classe mae
    def __init__(self, nome, ano, duracao): #o contrutor continua trazendo os atributos, mas nao precisa declarar todos
        super().__init__(nome, ano) #esses 2 ja estao declarados
        self.duracao = duracao

    def imprime(self):
        print(f'{self.nome} - Ano: {self.ano} - Duração: {self.duracao} - Likes {self.likes}')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas  = temporadas

    def imprime(self):
        print(f'{self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes {self.likes}')


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
for i in range(144):
    vingadores.likes_increase()

atlanta = Serie('atlanta', 2018, 2)
for i in range(720):
    atlanta.likes_increase()

house = Serie("house", 2005, 9)
for i in range(402):
    house.likes_increase()

filmes_e_series = [vingadores, atlanta, house]

for programa in filmes_e_series:
    programa.imprime()