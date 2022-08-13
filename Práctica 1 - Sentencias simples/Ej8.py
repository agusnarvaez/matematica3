""" 
    8.  Escribe un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule
        el índice de masa corporal, lo almacene en una variable, y muestre por pantalla redondeado 
        con dos decimales.
"""

# Importo librería math
import math

#Definición de función main
def main():
    

    print("Ejercicio 7 - Sentencias simples")
    print()
    
    # Leer valores
    peso = float(input("Ingrese peso en kg: "))
    estatura = float(input("Ingrese estatura en metros: "))
    
    # Calculo índice de masa corporal con peso y estatura
    indiceMasaCorporal = peso/(estatura**2)

    # Muestro índice de masa corporal redondeado
    print(f"El índice de masa corporal (IMC) es: {round(indiceMasaCorporal,2)}")

    print()
    print("Fin de programa!")

if __name__ == "__main__":
    main()
