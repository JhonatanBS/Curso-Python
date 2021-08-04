
def menu():
    print("\nMenu\n 1 - Soma de 2 números.\n 2 - Diferença entre 2 números (maior pelo menor).")
    print(" 3 - Produto entre 2 números.\n 4 - Divisão entre 2 números (o denominador não pode ser zero) .\n")
    numero = int(input("Escolha uma opção:"))

    return numero


def opcao(n, num1, num2):
    if n == 1:
        resultado = num1 + num2
        print(f"A soma entre os dois números é {resultado}")
    elif n == 2:
        if num1 > num2:
            resultado = num1 - num2 
        elif num1 < num2:
            resultado = num2 - num1
        else:
            resultado = 0
        print(f"A diferença entre os dois números é {resultado}")
    elif n == 3:
        resultado = num1 * num2
        print(f"O produto entre os dois número é {resultado}")       
    elif n == 4:
        if num2 != 0:
            resultado = float(num1) / float (num2)
            print(f"A divisão entre os dois números é {resultado}")
        else:
            print("Erro: o denominador não pode ser zero!")
    else:
        print("Opção Inválida!")        


valor1 = int(input("Digite o primeiro número:"))
valor2 = int(input("Digite o segundo número:"))
opcao(menu(), valor1, valor2)
