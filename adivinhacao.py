import random

print("*===================================*")
print("Seja bem-vindo ao jogo de Adivinhação!")
print("*===================================*")

secret_num = random.randrange(1, 11)
total_tentativas = 5
rodada = 1

for rodada in range(rodada, total_tentativas + 1):
    print("{} de {} tentativas.".format(rodada, total_tentativas))
    num_str = input("Escolha um número de 0 a 10: ")
    num_user = int(num_str)

    print("Você escolheu o número", num_user, end=".\n")

    if(num_user < 0 or num_user > 10):
        print("Você não pode digitar 0 ou 10, escolha outro número.")
        continue

    acertou = secret_num == num_user
    chute_maior = num_user > secret_num
    chute_menor = secret_num > num_user

    if(acertou):
        print("PARABÉNS!")
        print("Você acertou, o número secreto era", secret_num)
        break

    else:
        if(chute_maior):
            print("Sua escolha é maior que o número, você não acertou :(")

        if(chute_menor):
            print("Sua escolha é menor que o número, você não acertou :(")

print("O jogo acabou.")