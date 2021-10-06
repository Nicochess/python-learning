def jogar():
    print("*===================================*")
    print("**Seja bem-vindo ao jogo da Forca!**")
    print("*===================================*")

    secret_word = "banana".upper()
    letras_corretas = [ "_" for letra in secret_word]

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        index = 0
        erros = 0
        
        for letra in secret_word:
            if(chute == letra):
                letras_corretas[index] = letra
                letras_faltando = letras_corretas.count("_")
                if(letras_faltando == 0):
                    print("Taraaaannnn, você ganhou!!!")
                    acertou = True
            else:
                erros += 1
            
            index = index + 1

        print("{} letras faltando.".format(letras_faltando))
        print("Jogando...")
        print(letras_corretas)

if(__name__ == "__main__"):
    jogar()