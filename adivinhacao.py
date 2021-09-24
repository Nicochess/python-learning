print("*===================================*")
print("Seja bem-vindo ao jogo de Adivinhação!")
print("*===================================*")

secret_num = 7

num_str = input("Escolha um número de 0 a 10: ")
num_user = int(num_str)

print("Você escolheu o número", num_user)

if(secret_num == num_user):
    print("Você acertou, o número secreto era", secret_num)
else:
    print("Você não acertou o número secreto :(")

print("O jogo acabou.")