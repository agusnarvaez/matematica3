""" 
    10.     Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés
        al año. Estos ahorros no se cobran hasta finales de año y se te suman al balance final de
        tu cuenta de ahorros.
            Escribe un programa que comience leyendo la cantidad de dinero depositada en la cuenta
        de ahorros. El programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer,
        segundo y tercer año. Redondea cada cantidad a dos decimales.
"""

# Importo librería math
import math

#Definición de función main
def main():
    

    print("Ejercicio 10 - Sentencias simples")
    print()
    
    # Leer valores
    dineroDepositado = float(input("Ingrese cantidad de dinero depositado: "))
    
    # Calculo ganancia generada con interés en el primer, segundo y tercer año
    INTERES = 1.04
    primerAnio = dineroDepositado*INTERES
    segundoAnio = primerAnio*INTERES
    tercerAnio = segundoAnio*INTERES

    # Muestro las ganancias generadas por año
    print(f"El ahorro durante el primer año es {round(primerAnio,2)}")
    print(f"El ahorro durante el segundo año es {round(segundoAnio,2)}")
    print(f"El ahorro durante el tercer año es {round(tercerAnio,2)}")

    print()
    print("Fin de programa!")

if __name__ == "__main__":
    main()
