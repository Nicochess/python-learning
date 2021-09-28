import random
def jogar():
    print("*===================================*")
    print("Seja bem-vindo ao jogo de Adivinhação!")
    print("*===================================*")

    secret_num = random.randrange(1, 101)
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível de dificuldade do jogo: "))

    if(nivel == 1):
        total_tentativas = 15
    elif(nivel == 2):
        total_tentativas = 10
    elif(nivel == 3):
        total_tentativas = 5

    for rodada in range(rodada, total_tentativas + 1):
        print("{} de {} tentativas.".format(rodada, total_tentativas))
        num_str = input("Escolha um número de 0 a 100: ")
        num_user = int(num_str)

        print("Você escolheu o número", num_user, end=".\n")

        if(num_user < 0 or num_user > 100):
            print("Você não pode digitar 0 ou 100, escolha outro número.")
            continue

        acertou = secret_num == num_user
        chute_maior = num_user > secret_num
        chute_menor = secret_num > num_user

        if(acertou):
            print("PARABÉNS!")
            print("Você acertou e fez {}!!!".format(pontos))
            break

        else:
            if(chute_maior):
                print("Sua escolha é maior que o número, você não acertou :(")

            elif(chute_menor):
                print("Sua escolha é menor que o número, você não acertou :(")
            
        pontos_perdidos = abs((secret_num - num_user) * 2)
        pontos = pontos - pontos_perdidos
            
    print("O jogo acabou.")

if(__name__ == "__main__"):
    jogar()
