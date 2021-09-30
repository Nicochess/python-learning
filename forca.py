def jogar():
    print("*===================================*")
    print("**Seja bem-vindo ao jogo da Forca!**")
    print("*===================================*")

    secret_word = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()
        index = 0
        
        for letra in secret_word:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {}, na posição {}".format(letra, index))
            index = index + 1
        print("Jogando...")

if(__name__ == "__main__"):
    jogar()