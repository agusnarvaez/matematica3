""" 
    3.    Qué resultados muestran las siguientes expresiones: 
        a) True == True != False 
        b) 1 < 2 < 3 < 4 < 5 
        c) ( 1 < 2 < 3 ) and ( 4 < 5 ) 
        d) 1 < 2 < 4 < 3 < 5 
        e) ( 1 < 2 < 4 ) and ( 3 < 5 )
"""
#Definición de función main
def main():
    print("Ejercicio 3 - Sentencias simples")
    # a) True == True != False 
    expresion = True == True != False
    print(f"a) True == True != False = {expresion}")

    # b) 1 < 2 < 3 < 4 < 5 
    expresion = 1 < 2 < 3 < 4 < 5 
    print(f"b) 1 < 2 < 3 < 4 < 5 = {expresion}")

    # c) ( 1 < 2 < 3 ) and ( 4 < 5 ) 
    expresion = (1<2<3) and (4<5)
    print(f"c) (1 < 2 < 3) and  (4 < 5) = {expresion}")

    # d) 1 < 2 < 4 < 3 < 5 
    expresion = 1 < 2 < 4 < 3 < 5 
    print(f"d) 1 < 2 < 4 < 3 < 5  = {expresion}")

    # e) ( 1 < 2 < 4 ) and ( 3 < 5 )
    expresion = ( 1 < 2 < 4 ) and ( 3 < 5 )
    print(f"e) ( 1 < 2 < 4 ) and ( 3 < 5 ) = {expresion}")
    
    print("Conclusión: Se pueden hacer cálculos booleanos sin problema")
    

if __name__ == "__main__":
    main()
