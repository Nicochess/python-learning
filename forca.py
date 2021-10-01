def jogar():
    print("*===================================*")
    print("**Seja bem-vindo ao jogo da Forca!**")
    print("*===================================*")

    secret_word = "banana"
    letras_corretas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()
        index = 0
        
        for letra in secret_word:
            if(chute.upper() == letra.upper()):
                letras_corretas[index] = letra
                letras_faltando = letras_corretas.count("_")
            index = index + 1

        print("{} letras faltando.".format(letras_faltando))
        print("Jogando...")
        print(letras_corretas)
        if(letras_faltando == 0):
            break

if(__name__ == "__main__"):
    jogar()