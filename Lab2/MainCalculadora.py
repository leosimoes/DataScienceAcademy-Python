from Calculadora import Calculadora

if __name__ == '__main__':
    print("** ** ** ** ** ** ** Calculadora ** ** ** ** ** ** ** **")
    calculadora = Calculadora()

    operacoes_dict = {
        'A': calculadora.somar,
        'B': calculadora.somar_varios,
        'C': calculadora.subtrair,
        'D': calculadora.subtrair_varios,
        'E': calculadora.multiplicar,
        'F': calculadora.multiplicar_varios,
        'G': calculadora.dividir
    }

    while True:
        opcoes = """
        ----------------------------------------------------------
        Escolha a operacao desejada:
        A) Soma dois números
        B) Soma vários números
        C) Subtrair dois números
        D) Subtrair vários números
        E) Multiplicar dois números
        F) Multiplicar vários números
        G) Dividir dois números (inteiros)
        
        X) Sair            
        """

        print(opcoes)
        opcao = input("\t\tOpção: ").upper()

        if opcao == 'X':
            print("\t\tFim da execução do programa")
            break

        elif opcao not in('A', 'B', 'C', 'D', 'E', 'F', 'G'):
            print("\t\tOpção inválida")
            continue

        numeros = input("\t\tDigite os números separados por vírgula: ").replace(' ', '').split(',')
        numeros = list(map(int, numeros))

        if opcao in ('B', 'F'):
            print("\t\tResultado: " + str(operacoes_dict[opcao](*numeros)))

        elif len(numeros) == 2 and opcao in ('A', 'C', 'E', 'G'):
            primeiro_termo = numeros[0]
            segundo_termo = numeros[1]
            print("\t\tResultado: " + str(operacoes_dict[opcao](primeiro_termo, segundo_termo)))

        elif opcao in ('D'):
            primeiro_termo = numeros[0]
            segundo_termo = numeros[1:]
            print("\t\tResultado: " + str(operacoes_dict[opcao](primeiro_termo, *segundo_termo)))

        else:
            pass





