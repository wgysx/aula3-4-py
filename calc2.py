def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "não é possível dividir por zero."
    else:
        return a / b

print("-----Calculadora-----")

n1 = float(input("informe o primeiro número: "))
n2 = float(input("informe o segundo número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = input("Digite o número da operação desejada: ")

if operacao == "1":
    resultado = soma(n1, n2)
    print("A soma é:", resultado)
elif operacao == "2":
    resultado = subtracao(n1, n2)
    print("A subtração é:", resultado)
elif operacao == "3":
    resultado = multiplicacao(n1, n2)
    print("A multiplicação é:", resultado)
elif operacao == "4":
    resultado = divisao(n1, n2)
    if resultado is not None:
        print("A divisão é:", resultado)
    else:
        print("Não é possível dividir por zero.")
else:
    print("Opção inválida.")