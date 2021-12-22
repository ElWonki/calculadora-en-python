import os
import math

#operaciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

input()
os.system('cls')

while True:
    print("Calculadora")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    opcion = input("ingrese el numero de la operacion a realizar")

    if opcion=="1":
        numero1 = float(input("Numero 1: "))
        numero2 = float(input("Numero 2: "))

        print("El resultado de la suma es: ",suma(numero1, numero2))

    elif opcion=="2":
        numero1 = float(input("Numero 1: "))
        numero2 = float(input("Numero 2: "))
        
        print("La resta es: ",resta(numero1, numero2))
