# Projeto 1 do do curso Fundamentos de Linguagem Python Para Análise de Dados
# e Data Science (Com ChatGPT) da DataScienceAcademy

import json
import random
from os import system, name

def limpar_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')

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

def substituir_letra(letra, palavra, posicao):
    return palavra[:posicao] + letra + palavra[posicao + 1:]

def iniciar():
    limpar_tela()
    desenhos_forcas = carregar_desenhos()
    chances = len(desenhos_forcas)
    palavras = carregar_palavras()
    #print("Palavras lidas no arquivo: " + palavras)
    palavra = random.choice(palavras).upper()
    #print("Palavra escolhida: " + palavra)
    return palavra, desenhos_forcas

def desenhar(desenhos, erro):
    print(desenhos[str(erro)])

def atualizar(palavra, desenhos):
    palavra_exibida = '_' * len(palavra)
    chances = len(desenhos)
    erros = 0
    letras_acertadas, letras_erradas = [], []

    while '_' in palavra_exibida and chances > erros:
        print("\n-----------------------------------")
        print("Palavra: " + palavra_exibida)
        letra = input("Digite uma letra: ").upper()
        if(letra in palavra):
            print("Acertou")
            letras_acertadas.append(letra)
            for posicao, char in enumerate(palavra):
                if char == letra:
                    palavra_exibida = substituir_letra(letra, palavra_exibida, posicao)
        else:
            print("Errou")
            desenhar(desenhos, erros)
            letras_erradas.append(letra)
            erros += 1

        if letras_erradas:
            print("\nLetras erradas: " + ", ".join(letras_erradas))

    if '_' not in palavra_exibida and chances > erros:
        print("\nParabéns!!! Você Ganhou.")
    else:
        print("\nQue Pena. Você Perdeu.")


if __name__ == "__main__":
    palavra, desenhos = iniciar()
    atualizar(palavra, desenhos)
