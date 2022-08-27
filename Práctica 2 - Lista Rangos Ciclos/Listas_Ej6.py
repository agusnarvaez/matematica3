"""
    6.  Escribe un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista
        igual a la primera, pero al revés (crear una lista distinta).
"""

#Definición de función main
from re import finditer

def main():

    print("Ejercicio 5 - Listas")

    print()

    cantidadDePalabras = int(input("Introduzca la cantidad de palabras que va a ingresar: "))
    
    listaPalabras= []
    

    for i in range(0, cantidadDePalabras):
        palabra=input("Ingrese palabra: ")
        listaPalabras.append(palabra)

    print(listaPalabras)

    print()

    listaPalabras.reverse()

    print(listaPalabras)

    print()

    print("Fin de programa")

if __name__ == "__main__":
    main()
