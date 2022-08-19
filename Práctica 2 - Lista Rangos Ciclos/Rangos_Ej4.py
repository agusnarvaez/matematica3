"""
    4.  Escribe un programa que pida dos números enteros (el segundo mayor que el primero) y emita listas
    de números consecutivos al derecho y al revés. 
"""

#Definición de función main
from re import finditer


def main():
    print("Ejercicio 4 - Listas Rangos Ciclos")
    print()

    inicioRango = int(input("Introduzca un número: "))

    finRango = int(input("Introduzca un número mayor: "))

    # Range crea un rango, range(inicio, fin, paso)
    rango=range(inicioRango,finRango)

    # Con list(rango) lo pasamos a formato lista
    lista=list(rango)

    # Invierte lista
    listaInvertida = lista[::-1] # De principio a fin, con paso -1

    print(lista)
    print(listaInvertida)

    print()
    print("Fin de programa")
    

if __name__ == "__main__":
    main()
