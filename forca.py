def jogar():
    import os

    intro()

    choice = int(input("Qual modo de jogo deseja jogar, contra a máquina (1), contra outro player(2) ? "))

    if(choice == 1):
        print("Este modo de jogo está em desenvolvimento ainda.")
    elif(choice == 2):
        print("Está na hora do desafiante escolher a palavra dele.")
        secret_word = input("Digite a palavra: ").strip().upper()
        os.system('cls')

        letras_corretas = create_word_place(secret_word)

        enforcou = False
        acertou = False

        while(not enforcou and not acertou):
            os.system("cls")
            chute = word_request(letras_corretas)
            index = 0
            
            for letra in secret_word:
                if(chute == letra):
                    letras_corretas[index] = letra
                    letras_faltando = letras_corretas.count("_")
                    if(letras_faltando == 0):
                        os.system("cls")
                        acertou = win(letras_corretas)

                index = index + 1

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

def win(letras_corretas):
    print(letras_corretas)
    print("Taraaaannnn, você ganhou!!!")
    return True

if(__name__ == "__main__"):
    jogar()