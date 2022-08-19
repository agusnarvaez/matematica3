"""
    3.  Escribe un programa que pida un número entero y emita una lista de números consecutivos del 0 al
    valor dado.
"""

#Definición de función main
def main():
    print("Ejercicio 3 - Listas Rangos Ciclos")
    print()

    finRango = int(input("Introduzca un número: "))

    # Range crea un rango, range(inicio, fin, paso)
    rango=range(0,finRango)

    # Con list(rango) lo pasamos a formato lista
    print(list(rango))

    print()
    print("Fin de programa")
    

if __name__ == "__main__":
    main()
