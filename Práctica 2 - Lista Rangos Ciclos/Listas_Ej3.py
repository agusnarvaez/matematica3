"""
   3.   Escribe un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y
        sustituya la primera  (que debe estar en la lista) por la segunda. Emitir la lista. 
"""

#Definición de función main
from re import finditer

def main():

    print("Ejercicio 3 - Listas")

    print()

    cantidadDePalabras = int(input("Introduzca la cantidad de palabras que va a ingresar: "))
    
    listaPalabras = []

    for i in range(0, cantidadDePalabras):
        palabra=input("Ingrese palabra: ")
        listaPalabras.append(palabra)

    print()

    print(listaPalabras)

    palabraAIngresar = input("Ingrese una palabara: ")

    palabraReemplazada = input("Ingrese una palabara: ")
    
    indice = listaPalabras.index(palabraReemplazada)

    listaPalabras.pop(indice)

    listaPalabras.insert(indice,palabraAIngresar)

    print(listaPalabras)

    print()

    print("Fin de programa")
    

if __name__ == "__main__":
    main()
