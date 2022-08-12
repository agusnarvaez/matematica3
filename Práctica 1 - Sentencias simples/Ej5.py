""" 
    5.    Desarrolla un programa que permita leer 2 valores y que emita por pantalla la suma, la resta,
    el producto, la división, el resto, el promedio y el doble producto del primero menos la mitad del
    segundo. 
"""

# Importo librería math
import math

#Definición de función main
def main():
    

    print("Ejercicio 5 - Sentencias simples")
    print()
    
    # Leer valores
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))

    suma = valor1 + valor2
    resta = valor1 - valor2
    producto = valor1*valor2
    division = valor1/valor2
    resto = valor1%valor2
    promedio = (valor1+valor2)/2
    resultado = 2*valor1 - valor2/2

    print(f"La suma de ambos números es: {suma}")
    print(f"La resta de ambos números es: {resta}")
    print(f"El producto de ambos números es: {producto}")
    print(f"La división de ambos números es: {division}")
    print(f"El resto de ambos números es: {resto}")
    print(f"El promedio de ambos números es: {promedio}")
    print(f"El doble producto del primero menos la mitad del segundo es: {resultado}")

    print()
    print("Fin de programa!")

if __name__ == "__main__":
    main()
