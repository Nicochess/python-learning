print("*===================================*")
print("Seja bem-vindo ao jogo de Adivinhação!")
print("*===================================*")

secret_num = 7
tentativas = 5

while(tentativas >= 0):
    num_str = input("Escolha um número entre 0 a 10: ")
    num_user = int(num_str)

    print("Você escolheu o número", num_user, end=".\n")

    acertou = secret_num == num_user
    chute_maior = num_user > secret_num
    chute_menor = secret_num > num_user

    if(acertou):
        print("Você acertou, o número secreto era", secret_num)
    elif(num_user  == 0 or num_user == 10):
        print("Você não pode digitar 0 ou 10.")
    else:
        print("Ainda tem mais", tentativas, "tentativas.")
        if(chute_maior):
            print("Sua escolha é maior que o número, você não acertou :(")
        if(chute_menor):
            print("Sua escolha é menor que o número, você não acertou :(")
        tentativas = tentativas - 1

print("O jogo acabou.")