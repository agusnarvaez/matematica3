"""
    6.   Escribe un programa que pida dos números enteros y emita la lista de números pares que hay
    entre ellos (incluidos ellos mismos si son pares) 
"""

#Definición de función main
from re import finditer


def main():
    print("Ejercicio 5 - Listas Rangos Ciclos")
    print()

    inicioRango = int(input("Introduzca un número: "))

    finRango = int(input("Introduzca otro número: "))

    # Range crea un rango, range(inicio, fin, paso)
    if(inicioRango%2!=0):
        inicioRango+=1
    elif(inicioRango==0):
        inicioRango+=2

    if(finRango%2==0):
        finRango+=2
    
    rango=range(inicioRango,finRango,2)
    # Con list(rango) lo pasamos a formato lista
    lista=list(rango)

    # Otra forma mas corta
    listaOtraForma = [x for x in range(inicioRango,finRango,2) if x%2==0] 
    
    print()
    print(lista)
    print()
    print(listaOtraForma)

    print()
    print("Fin de programa")
    

if __name__ == "__main__":
    main()
