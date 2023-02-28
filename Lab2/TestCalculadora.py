import unittest
from Calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        calculadora = Calculadora()

        self.assertEqual(3, calculadora.somar(0, 3))
        self.assertEqual(5, calculadora.somar(3, 2))
        self.assertEqual(5, calculadora.somar(2, 3))
        self.assertEqual(0, calculadora.somar(-1, 1))
        self.assertEqual(200, calculadora.somar(100, 100))

    def test_somar_varios(self):
        calculadora = Calculadora()

        self.assertEqual(3, calculadora.somar_varios(0, 3))
        self.assertEqual(5, calculadora.somar_varios(3, 2))
        self.assertEqual(5, calculadora.somar_varios(2, 3))
        self.assertEqual(0, calculadora.somar_varios(-1, 1))
        self.assertEqual(200, calculadora.somar_varios(100, 100))

        self.assertEqual(300, calculadora.somar_varios(100, 100, 100))
        self.assertEqual(400, calculadora.somar_varios(100, 100, 100, 100))
        self.assertEqual(500, calculadora.somar_varios(100, 100, 100, 100, 100))

    def test_subtrair(self):
        calculadora = Calculadora()

        self.assertEqual(3, calculadora.subtrair(3, 0))
        self.assertEqual(1, calculadora.subtrair(3, 2))
        self.assertEqual(-2, calculadora.subtrair(-1, 1))
        self.assertEqual(0, calculadora.subtrair(100, 100))

    def test_subtrair_varios(self):
        calculadora = Calculadora()

        self.assertEqual(3, calculadora.subtrair_varios(3, 0))
        self.assertEqual(1, calculadora.subtrair_varios(3, 2))
        self.assertEqual(-2, calculadora.subtrair_varios(-1, 1))
        self.assertEqual(0, calculadora.subtrair_varios(100, 100))

        self.assertEqual(800, calculadora.subtrair_varios(1000, 100, 100))
        self.assertEqual(700, calculadora.subtrair_varios(1000, 100, 100, 100))
        self.assertEqual(600, calculadora.subtrair_varios(1000, 100, 100, 100, 100))

    def test_multiplicar(self):
        calculadora = Calculadora()

        self.assertEqual(0, calculadora.multiplicar(0, 3))
        self.assertEqual(3, calculadora.multiplicar(1, 3))
        self.assertEqual(6, calculadora.multiplicar(3, 2))
        self.assertEqual(6, calculadora.multiplicar(2, 3))
        self.assertEqual(-1, calculadora.multiplicar(-1, 1))
        self.assertEqual(10000, calculadora.multiplicar(100, 100))

    def test_multiplicar_varios(self):
        calculadora = Calculadora()

        self.assertEqual(0, calculadora.multiplicar_varios(0, 3))
        self.assertEqual(3, calculadora.multiplicar_varios(1, 3))
        self.assertEqual(6, calculadora.multiplicar_varios(3, 2))
        self.assertEqual(6, calculadora.multiplicar_varios(2, 3))
        self.assertEqual(-1, calculadora.multiplicar_varios(-1, 1))
        self.assertEqual(10000, calculadora.multiplicar_varios(100, 100))

        self.assertEqual(1000, calculadora.multiplicar_varios(10, 10, 10))
        self.assertEqual(1000, calculadora.multiplicar_varios(10, 10, 10, 1))
        self.assertEqual(10000, calculadora.multiplicar_varios(10, 10, 10, 10))
        self.assertEqual(100000, calculadora.multiplicar_varios(10, 10, 10, 10, 10))

    def test_dividir(self):
        calculadora = Calculadora()

        self.assertEqual(3, calculadora.dividir(3, 1))
        self.assertEqual(-3, calculadora.dividir(3, -1))
        self.assertEqual(-3, calculadora.dividir(-3, 1))
        self.assertEqual(3, calculadora.dividir(-3, -1))
        self.assertEqual(1, calculadora.dividir(10, 10))

        self.assertIsNone(calculadora.dividir(10, 0))


if __name__ == '__main__':
    unittest.main()
