"""
   2.   Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga
        cuántas veces aparece esa palabra en la lista. 
"""

#Definición de función main
from re import finditer

def main():

    print("Ejercicio 2 - Listas")

    print()

    cantidadDePalabras = int(input("Introduzca la cantidad de palabras que va a ingresar: "))
    
    listaPalabras = []

    for i in range(0, cantidadDePalabras):
        palabra=input("Ingrese palabra: ")
        listaPalabras.append(palabra)

    print()

    print(listaPalabras)

    palabraABuscar = input("Ingrese una palabara: ")

    cantidad = 0

    for i in range(0, cantidadDePalabras):
        if palabraABuscar in listaPalabras[i]:
            cantidad+=1

    print()

    print(f"Su palabra aparece en la lista {cantidad} veces")

    print("Fin de programa")
    

if __name__ == "__main__":
    main()
