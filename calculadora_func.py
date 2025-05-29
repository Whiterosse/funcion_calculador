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
            return "Operacion invalida"
        return num1 / num2
    else:
        return "Error de datos"
    
num1 = float(input("Ingresa el valor 1: "))
num2 = float(input("Ingresa el dato a evaluar: "))
operacion = input("Ingresa el tipo de operacion: + , - , * , / ")
print("El resultado es: " , calculadora(num1,num2,operacion))

while True:
    operacion = input("Ingresa la operación (+, -, *, /) o escribe 'salir' para terminar: ")
    
    if operacion.lower() == "salir":
        print("Calculadora finalizada. ¡Hasta luego!")
        break

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: Debes ingresar números válidos.")
        continue

    resultado = calculadora(num1, num2, operacion)
    print("Resultado:", resultado)
    print("-" * 30)

