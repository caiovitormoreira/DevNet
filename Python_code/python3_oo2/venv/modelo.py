class Filme:
    def __init__(self, nome, ano, duracao, likes):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

class Serie:
    def __init__(self, nome, ano, temporadas, likes=0):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def likes_increase(self):
        self.likes += 1


house = Serie("house", 2005, 9)
hymym = Serie("How I met your Mother", 2003, 8)
print(f'nome:{hymym.nome} - Ano: {hymym.ano} - Temporadas: {hymym.temporadas} - Likes: {hymym.likes}')