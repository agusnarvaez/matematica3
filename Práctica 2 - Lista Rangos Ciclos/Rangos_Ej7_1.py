"""
    7.  Escribe tres programas que emitan las siguientes secuencias de números: 
        •   En el primer programa, el tipo range() que se utilice en cada bucle debe tener un único argumento. 
        •   En el segundo programa, el tipo range() que se utilice en cada bucle debe tener dos argumentos. 
        •   En el tercer programa, el tipo range() que se utilice en cada bucle debe tener tres argumentos.
"""

#Definición de función main
from re import finditer


def main():

    print("Ejercicio 7_1 - Listas Rangos Ciclos")

    print()

    finRango = int(input("Introduzca un número: "))
    
    rango=range(finRango)

    # Con list(rango) lo pasamos a formato lista
    lista=list(rango)

    print()
    
    print(lista)

    print()

    print("Fin de programa")
    

if __name__ == "__main__":
    main()
