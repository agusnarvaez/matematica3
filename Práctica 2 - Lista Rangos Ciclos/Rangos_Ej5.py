"""
    5.  Escribe un programa que pida dos números enteros y emita la lista de números consecutivos que hay
    entre ellos, de menor a mayor. 
"""

#Definición de función main
from re import finditer


def main():
    print("Ejercicio 5 - Listas Rangos Ciclos")
    print()

    inicioRango = int(input("Introduzca un número: "))

    finRango = int(input("Introduzca otro número: "))

    # Range crea un rango, range(inicio, fin, paso)
    rango=range(inicioRango,finRango)

    # Con list(rango) lo pasamos a formato lista
    lista=list(rango)

    lista.pop(0)
    print(lista)

    print()
    print("Fin de programa")
    

if __name__ == "__main__":
    main()
