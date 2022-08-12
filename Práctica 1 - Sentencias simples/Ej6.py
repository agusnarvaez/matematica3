""" 
    6.  Desarrolla un programa que dada una cierta cantidad de galones, los convierta a litros
        y dada una medida en millas las convierta a metros, ambos con entrada de tipo flotante.
"""

# Importo librería math
import math

#Definición de función main
def main():
    

    print("Ejercicio 6 - Sentencias simples")
    print()
    
    # Leer valores
    galones = float(input("Ingrese galones: "))
    millas = float(input("Ingrese millas: "))

    # Convierto galones a litros
    litros = galones*3.78541

    # Convierto millas a metros
    metros = millas*1609.34

    print(f"{galones} galones son {litros} litros")
    print(f"{millas} millas son {metros} metros")

    print()
    print("Fin de programa!")

if __name__ == "__main__":
    main()
