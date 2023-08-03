def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def calcular():
    print("Calculadora Básica")
    print("Operaciones disponibles: +, -, *, /")
    num1 = float(input("Ingresa el primer número: "))
    operador = input("Ingresa el operador: ")
    num2 = float(input("Ingresa el segundo número: "))

    if operador == '+':
        resultado = sumar(num1, num2)
    elif operador == '-':
        resultado = restar(num1, num2)
    elif operador == '*':
        resultado = multiplicar(num1, num2)
    elif operador == '/':
        resultado = dividir(num1, num2)
    else:
        resultado = "Operador inválido"

    print(f"El resultado de la operación es: {resultado}")

calcular()
