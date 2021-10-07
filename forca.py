def jogar():
    import os

    print("*===================================*")
    print("**Seja bem-vindo ao jogo da Forca!**")
    print("*===================================*")

    choice = int(input("Qual modo de jogo deseja jogar, contra a máquina (1), contra outro player(2) ? "))

    if(choice == 1):
        print("Este modo de jogo está em desenvolvimento ainda.")
    elif(choice == 2):
        print("Está na hora do desafiante escolher a palavra dele.")
        secret_word = input("Digite a palavra: ").strip().upper()
        os.system('cls')
        letras_corretas = [ "_" for letra in secret_word]

        enforcou = False
        acertou = False

        while(not enforcou and not acertou):
            os.system("cls")
            print(letras_corretas)
            chute = input("Qual letra? ")
            chute = chute.strip().upper()
            index = 0
            
            for letra in secret_word:
                if(chute == letra):
                    letras_corretas[index] = letra
                    letras_faltando = letras_corretas.count("_")
                    if(letras_faltando == 0):
                        os.system("cls")
                        print(letras_corretas)
                        print("Taraaaannnn, você ganhou!!!")
                        acertou = True
                index = index + 1

if(__name__ == "__main__"):
    jogar()