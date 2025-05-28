'''Descripción:

Escribe un programa en Python que realice operaciones matemáticas simples (suma, resta, multiplicación y división) 
utilizando una función.
El programa debe permitir al usuario ingresar dos números y seleccionar una operación para realizar.
'''

def calculadora(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 == 0:
            return "Valor errado,  divisor no puede ser cero (0)"
        return num1 / num2
    else:
        return "Operacion invalida"

num1 = float(input("Ingresa el valor 1: "))
num2 = float(input("Ingresa el valor 2: "))
operacion = (input("Ingresa el tipo de operacion: "))

print("Resultado es: " , calculadora(num1, num2, operacion))

