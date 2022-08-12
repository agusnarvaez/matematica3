""" 
    7.  Realiza un programa que dadas una cantidad de segundos los convierta en horas, minutos y segundos.
"""

# Importo librería math
import math

#Definición de función main
def main():
    

    print("Ejercicio 7 - Sentencias simples")
    print()
    
    # Leer valores
    segundos = float(input("Ingrese segundos: "))
    

    # Convierto segundos a minutos

    minutos = segundos/60
    minutos= int(segundos/60)
    horas = int(minutos/60)
    segundos = int(segundos%60)
    minutos = int(minutos%60)

    print(f"Su hora da: {horas}:{minutos}:{segundos}")

    print()
    print("Fin de programa!")

if __name__ == "__main__":
    main()
