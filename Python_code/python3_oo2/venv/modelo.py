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

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas  = temporadas


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.likes_increase()
vingadores.likes_increase()
vingadores.likes_increase()

atlanta.likes_increase()
atlanta.likes_increase()

print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')

# house = Serie("house", 2005, 9)
# chequemate = Filme("cheque mate", 2010, 130)
# print(f'nome: {house.nome} - Ano: {house.ano} - Temporadas: {house.temporadas} - Likes: {house.likes}')
# print(f'nome: {chequemate.nome} - Ano: {chequemate.ano} - Temporadas: {chequemate.temporadas} - Likes: {chequemate.likes}')