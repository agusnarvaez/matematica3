"""
    2.    Escribe un tipo range() que emita: [-50, -2050, -4050, -6050]
"""

#Definición de función main
def main():
    print("Ejercicio 1 - Listas Rangos Ciclos")
    print()

    # Range crea un rango, range(inicio, fin, paso)
    rango=range(-50,-6100,-2000)

    # Con list(rango) lo pasamos a formato lista
    print(list(rango))

    print()
    print("Fin de programa")
    

if __name__ == "__main__":
    main()
