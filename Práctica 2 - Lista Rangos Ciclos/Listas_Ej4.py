"""
   4.   Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y 
        elimine esa palabra de la lista. 
"""

#Definición de función main
from re import finditer

def main():

    print("Ejercicio 4 - Listas")

    print()

    cantidadDePalabras = int(input("Introduzca la cantidad de palabras que va a ingresar: "))
    
    listaPalabras = []

    for i in range(0, cantidadDePalabras):
        palabra=input("Ingrese palabra: ")
        listaPalabras.append(palabra)

    print()

    print(listaPalabras)

    palabraAEliminar = input("Ingrese una palabara: ")
    
    indice = listaPalabras.index(palabraAEliminar)

    listaPalabras.pop(indice)

    print(listaPalabras)

    print()

    print("Fin de programa")

if __name__ == "__main__":
    main()
