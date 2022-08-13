""" 
    9.  Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer
        venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben
        calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso
        pesa 112 g y cada muñeca 75 g. Escribe un programa que lea el número de payasos y muñecas
        vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""

# Importo librería math
import math

#Definición de función main
def main():
    

    print("Ejercicio 9 - Sentencias simples")
    print()
    
    # Leer valores
    payasos = int(input("Ingrese cantidad de payasos: "))
    muñecas = int(input("Ingrese cantidad de muñecas: "))
    
    # Calculo peso total del paquete
    pesoTotal = payasos*112 + muñecas*75

    # Muestro peso total del paquete
    print(f"El peso total del paquete es {pesoTotal} g")

    print()
    print("Fin de programa!")

if __name__ == "__main__":
    main()
