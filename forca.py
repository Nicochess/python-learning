def jogar():
    import os

    intro()

    choice = int(input("Qual modo de jogo deseja jogar, contra a máquina (1), contra outro player(2) ? "))

    if(choice == 1):
        print("Este modo de jogo está em desenvolvimento ainda.")
    elif(choice == 2):
        print("Está na hora do desafiante escolher a palavra dele.")
        secret_word = input("Digite a palavra: ").strip().upper()
        tip = input("Dê uma dica simples: ").upper()
        os.system('cls')

        letras_corretas = create_word_place(secret_word)

        enforcou = False
        acertou = False
        erros = 0
        tentativas = []

        while(not enforcou and not acertou):
            print(tip)
            desenhar_forca(erros, tentativas)
            chute = word_request(letras_corretas)
            tentativas.append(chute)

            if(chute in secret_word):
                chute_certo(secret_word, chute, letras_corretas)
                os.system("cls")
            else:
                erros += 1
                desenhar_forca(erros, tentativas)
                os.system("cls")

            enforcou = erros == 7
            acertou = "_" not in letras_corretas

        if(acertou):
            you_win()
        else:
            desenhar_forca(erros, tentativas)
            print("A palavra era {}".format(secret_word))
            print("Você perdeu, tente de novo :(")

def intro():
    print("*===================================*")
    print("**Seja bem-vindo ao jogo da Forca!**")
    print("*===================================*")

def create_word_place(secret_word):
    return [ "_" for letra in secret_word]

def word_request(letras_corretas):
    print(letras_corretas)
    chute = input("Qual letra? ")
    return chute.strip().upper()

def chute_certo(secret_word, chute, letras_corretas):
    index = 0
    for letra in secret_word:
        if(chute == letra):
            letras_corretas[index] = letra
        index += 1

def you_win():
    print("   _________   ")
    print(" _|         |_ ")
    print("| |         | |")
    print(" -|         |- ")
    print("   \       /   ")
    print("    \     /    ")
    print("   __\___/__   ")
    print("  |_________|   ")
    print("Taraaaannnn, você ganhou!!!")

def desenhar_forca(erros, tentativas):
    print("__________     ")
    print("|        |   {}".format(tentativas))
    print("|        |     ")

    if(erros == 0):
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")

    if(erros == 1):
        print("|       (_)    ")
        print("|              ")
        print("|              ")
        print("|              ")

    if(erros == 2):
        print("|       (_)    ")
        print("|        |     ")
        print("|              ")
        print("|              ")

    if(erros == 3):
        print("|       (_)    ")
        print("|        |     ")
        print("|        |     ")
        print("|              ")

    if(erros == 4):
        print("|       (_)    ")
        print("|        |     ")
        print("|        |     ")
        print("|       /      ")

    if(erros == 5):
        print("|       (_)    ")
        print("|        |     ")
        print("|        |     ")
        print("|       / \    ")

    if(erros == 6):
        print("|       (_)    ")
        print("|        |/    ")
        print("|        |     ")
        print("|       / \    ")

    if(erros == 7):
        print("|       (_)    ")
        print("|       \|/    ")
        print("|        |     ")
        print("|       / \    ")

    print("|___________   ")

if(__name__ == "__main__"):
    jogar()