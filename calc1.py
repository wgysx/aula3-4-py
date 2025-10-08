print("-----Calculadora-----")

n1 = float(input("informe o primeiro número: "))
n2 = float(input("informe o segundo número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
op = input("Digite o número da operação desejada: ")

if op == "1":
    resultado = n1 + n2
    print("A soma é:", resultado)
elif op == "2":
    resultado = n1 - n2
    print("A subtração é:", resultado)
elif op == "3":
    resultado = n1 * n2
    print("A multiplicação é:", resultado)
elif op == "4":
    if n2 != 0:
        resultado = n1 / n2
        print("A divisão é:", resultado)
    else:
        print("Não é possível dividir por zero.")
else:
    print("Opção inválida.")