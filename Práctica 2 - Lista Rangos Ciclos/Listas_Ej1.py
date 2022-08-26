"""
    1.  Escribe un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un
        número y luego solicitar esa cantidad de palabras para crear la lista. Por último, el programa tiene que
        emitir la lista. 
"""

#Definición de función main
from re import finditer

def main():

    print("Ejercicio 1 - Listas")

    print()

    cantidadDePalabras = int(input("Introduzca la cantidad de palabras que va a ingresar: "))
    
    listaPalabras = []

    for i in range(0, cantidadDePalabras):
        palabra=input("Ingrese palabra: ")
        listaPalabras.append(palabra)

    print()
    
    print(listaPalabras)

    print()

    print("Fin de programa")
    

if __name__ == "__main__":
    main()
