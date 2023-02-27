import json, random
from Hangman import Hangman

def carregar_desenhos():
    desenhos_forcas = []
    with open('desenhosDaForca.json') as arquivo:
        desenhos_forcas = json.load(arquivo)
    return desenhos_forcas

def carregar_palavras():
    palavras = []
    with open('palavras.json') as arquivo:
        palavras = json.load(arquivo).get("palavras")
    return palavras


if __name__ == '__main__':
    palavras = carregar_palavras()
    desenhos = carregar_desenhos()
    palavra = random.choice(palavras).upper()

    hangman = Hangman(palavra, desenhos)
    #hangman = Hangman()

    while not hangman.is_terminado():
        hangman.mostrar_letras()
        hangman.adivinhar_letra()

    hangman.mostrar_palavra()

    if hangman.venceu():
        print("\nParabéns!!! Você Ganhou.")
    else:
        print("\nQue Pena... Você Perdeu.")