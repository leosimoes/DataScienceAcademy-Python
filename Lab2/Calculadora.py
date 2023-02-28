import operator
from functools import reduce

class Calculadora():

    def __init__(self):
        pass

    def somar(self, parcela1, parcela2):
        return parcela1 + parcela2

    def somar_varios(self, * parcelas):
        return sum(parcelas)

    def subtrair(self, minuendo, subtraendo):
        return minuendo - subtraendo

    def subtrair_varios(self, minuendo, * subtraendos):
        return reduce(operator.sub, subtraendos, minuendo)

    def multiplicar(self, parcela1, parcela2):
        return parcela1 * parcela2

    def multiplicar_varios(self, * parcelas):
        return reduce(operator.mul, parcelas, 1)

    def dividir(self, dividendo, divisor):
        if(divisor != 0):
            return int(dividendo / divisor)
        else:
            return None
