"""
    7.  Escribe tres programas que emitan las siguientes secuencias de números: 
        •   En el primer programa, el tipo range() que se utilice en cada bucle debe tener un único argumento. 
        •   En el segundo programa, el tipo range() que se utilice en cada bucle debe tener dos argumentos. 
        •   En el tercer programa, el tipo range() que se utilice en cada bucle debe tener tres argumentos.
"""

#Definición de función main
from re import finditer

def main():

    print("Ejercicio 7_3 - Listas Rangos Ciclos")

    print()

    inicioRango = int(input("Introduzca un número: "))
    
    finRango = int(input("Introduzca un número: "))

    paso = int(input("Introduzca un número: "))
    
    rango=range(inicioRango,finRango,paso)

    # Con list(rango) lo pasamos a formato lista
    lista=list(rango)

    print()
    
    print(lista)

    print()

    print("Fin de programa")
    

if __name__ == "__main__":
    main()
