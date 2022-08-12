"""
    1- Declaraciones sencillas e input
    Se utilizan estas comillas para realizar comentarios en mas de una línea
"""
# Comentarios en una línea #

#Definición de función main
def main():
    print("Ejercicio 1 - Sentencias simples")
    # Input 
    tuNombre = input("Ingresá tu nombre: ")
    # Output con variable usando f
    print(f"Tu nombre es {tuNombre}")

    # Output con variable SIN usar f
    print("Tu nombre es ",tuNombre)

    # Hacemos un sencillo ejemplo con productos y sus precios

    producto1 = input("Ingrese Producto 1: ")
    # Aclaro que es un entero con int()
    precio1 = int(input("Ingrese precio de producto 1: "))
    producto2 = input("Ingrese Producto 2: ")
    precio2 = int(input("Ingrese precio de producto 2: "))

    # Declaramos una constante, es una buena práctica declararlas en mayúsculas
    BONIFICACION = 20

    # Sumamos los dos precios y los guardamos en una variable
    precioTotal = precio1 + precio2
    print(f"El precio total es: {precioTotal}")
    print("El precio total es: ",precioTotal)
    print(f"Es el resultado de la suma de los productos 1 {producto1} y producto2 {producto2}")

    # Otra forma de mostrar el precio total
    print("El precio total es: " + str(precioTotal))

    # Operador de asignación
    precioTotal += BONIFICACION

    print("El precio con bonificación(20) es:", precioTotal)
    


if __name__ == "__main__":
    main()
