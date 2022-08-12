""" 
    4.    Qué resultados se obtendrán al evaluar las siguientes expresiones. Recuerda usar import
    math puedes consultar: https://docs.python.org/3/library/math.html 

        a) int ( exp( 2 * log(3)) ) 
        b) round ( 4 * sin(3 * pi / 2 ) ) 
        c) abs ( log10(.01) * sqrt(25) ) 
        d) round ( 3.21123 * log10(1000), 3)
"""

# Importo librería math
import math

#Definición de función main
def main():
    

    print("Ejercicio 4 - Sentencias simples")
    print()
    # a) int ( exp( 2 * log(3)) ) 
    expresion = int(math.exp(2 * math.log(3)))
    print(f"a) int ( math.exp(2* math.log(3)) = {expresion}")

    # b) round ( 4 * math.sin(3 * math.pi / 2 ) ) 
    expresion = round(4 * math.sin(3 * math.pi / 2))
    print(f"b) round ( math.sin(3* math.pi / 2) = {expresion}")

    # c) abs( math.log10(.01) * math.sqrt(25) )
    expresion = abs(math.log10(.01) * math.sqrt(25))
    print(f"c) abs ( math.log10(.01) * math.sqrt(25)) = {expresion}")

    # d) round ( 3.21123 * math.log10(1000), 3)
    expresion = round(3.21123 * math.log10(1000), 3)
    print(f"d) round ( 3.21123 * math.log10(1000), 3) = {expresion}")
    print()
    print("Conclusión: Para definir una librería fuera de la función main y para llamar a ciertos métodos de la librería, tengo que llamarla directamente, por ejemplo librería.método()")

if __name__ == "__main__":
    main()
