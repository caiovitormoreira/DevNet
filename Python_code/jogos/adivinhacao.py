print("Bem vindo ao jogo de adivinhação")

numero_secreto = 42

numero_de_tentativa = 5
rodada = 1

for rodada in range(1, numero_de_tentativa+1):
    print("Tentativa {} de {}".format(rodada, numero_de_tentativa))

    chute = input("Digite um numero entre 1 e 100: ")
    chute = int(chute)
    if (chute < 1 or chute > 100):
        print("Sua mula, o numero deve ser entre 1 e 100.")
        continue
    if (numero_secreto == chute):
        print('voce acertou o maldito do numero')
        break
    else:
        if(chute > numero_secreto):
            print('seu chute foi maior do que o numero secreto')
        elif(chute < numero_secreto):
            print('seu chute foi menor do que o numero secreto')

print("Fim de jogo")