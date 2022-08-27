"""
    5.  Escribe un programa que permita crear dos listas de palabras y que, a continuación, elimine de la 
        primera lista los nombres de la segunda lista. 
"""

#Definición de función main
from re import finditer

def main():

    print("Ejercicio 5 - Listas")

    print()

    cantidadDePalabras = int(input("Introduzca la cantidad de palabras que va a ingresar: "))
    
    listaPalabras1 = []
    listaPalabras2 = []

    for i in range(0, cantidadDePalabras):
        palabra=input("Ingrese palabra: ")
        listaPalabras1.append(palabra)

    for i in range(0, cantidadDePalabras):
        palabra=input("Ingrese palabra: ")
        listaPalabras2.append(palabra)

    print()

    print(listaPalabras1)
    for i in range(0, cantidadDePalabras):
        if listaPalabras2[i] in listaPalabras1:
            listaPalabras1.remove(listaPalabras2[i])

    print(listaPalabras1)

    print()

    print("Fin de programa")

if __name__ == "__main__":
    main()
