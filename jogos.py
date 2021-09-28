import forca
import adivinhacao
def escolher_jogo():
    print("*===================================*")
    print("Seja bem-vindo a biblioteca de Jogos!")
    print("*===================================*")

    print("(1)Jogo da Forca (2) Jogo de Adivinhação")
    jogo = int(input("Qual jogo deseja jogar? "))

    if(jogo == 1):
        forca.jogar()
    if(jogo == 2):
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolher_jogo()