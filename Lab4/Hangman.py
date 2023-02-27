# Classe
class Hangman():

    # Método Construtor
    def __init__(self, palavra, desenhos):
        self.palavra = palavra
        self.palavra_exibida = '_' * len(palavra)
        self.desenhos = desenhos
        self.chances = len(desenhos)
        self.erros = 0
        self.letras_acertadas = []
        self.letras_erradas = []
        #print(self.palavra)

    # Método para adivinhar a letra
    def adivinhar_letra(self):
        letra = input("Digite uma letra: ").upper()

        if(letra in self.palavra):
            print("Acertou")
            self.letras_acertadas.append(letra)
            for posicao, char in enumerate(self.palavra):
                if char == letra:
                    self.palavra_exibida = self.palavra_exibida[:posicao] + letra + self.palavra_exibida[posicao + 1:]
        else:
            print("Errou")
            print(self.desenhos[str(self.erros)])
            self.letras_erradas.append(letra)
            self.erros += 1
            self.chances -= 1


    # Método para verificar se o jogo terminou
    def is_terminado(self):
        return self.chances == 0 or self.palavra == self.palavra_exibida or self.erros > 6

    # Método para verificar se o jogador venceu
    def venceu(self):
        return self.chances > 0 or self.palavra == self.palavra_exibida or self.erros < 6

    # Método para mostrar a letra no board
    def mostrar_letras(self):
        print("\n-----------------------------------")
        print("Palavra: " + self.palavra_exibida)
        if self.letras_erradas:
            print("\nLetras erradas: " + ", ".join(self.letras_erradas))

    # Método para mostrar a palavra
    def mostrar_palavra(self):
        print("\n-----------------------------------")
        print("Palavra: " + self.palavra)

