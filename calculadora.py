# Calculadora
while True:
    print("\nCalculadora")
    num1 = float(input("Digite o primeiro número: "))

    print("\nEscolha a operação:")
    print("+ para Soma")
    print("- para Subtração")
    print("* para Multiplicação")
    print("/ para Divisão")

    operacao = input("Digite a operação desejada: ")

    num2 = float(input("Digite o segundo número: "))

    # Condicional para executar a operação
    if operacao == "+":
        resultado = num1 + num2
        print("Resultado:", resultado)

    elif operacao == "-":
        resultado = num1 - num2
        print("Resultado:", resultado)

    elif operacao == "*":
        resultado = num1 * num2
        print("Resultado:", resultado)

    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Erro: divisão por zero!")

    else:
        print("Operação inválida!")

    # Perguntar se deseja continuar
    continuar = input("\nDeseja fazer outra operação? (S/N): ")

    if continuar != "S":
        print("Calculadora encerrada.")
        break
