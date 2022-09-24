"""
En una escuela de 1000 alumnos, se han evaluado literatura, matemática y biología, obteniendose los siguientes resultados:


# 680 aprobaron literatura y los datos se recolectaron en un diccionario
literatura = {"Romántica": 40, "Clásica": 118, "Fantástica": 50, "Moderna": 95,
"Antigua": 56, "Poesía":  131, "Cuento": 103, "Novela": 87}

# 320 aprobaron biología y los datos se recolectaron en una tupla
biología = (40, 50, 60, 75, 34, 61)

# 490 opinaron sobre Educación
matemática = [34, 40, 61, 75, 87, 90, 103]
   
Responeder:
    a) Cuántos aprobaron biología, matemática y literatura
    b) Cuántos aprobaron solo literatura y matemática?
    c) Cuantos aprobaron sólo literatura?
    d) Cuántos aprobaron sólo biología?
    e) Cuántos aprobaron sólo matemática?
    f) Cuántos aprobaron 2 de los 3 exámenes?
"""

from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles


lista_matematica = [34, 40, 61, 75, 87, 90, 103]
tupla_biologia = (40, 50, 60, 75, 34, 61)
diccio_literatura = {"Romántica": 40, "Clásica": 118, "Fantástica": 50, "Moderna": 95,
"Antigua": 56, "Poesía":  131, "Cuento": 103, "Novela": 87}

""" def sumaSet(setASumar):
    suma = 0
    for id,elemento in setASumar:
            suma += elemento
    return set(suma) """

#* Defino variables globales
universal = 1000
ninguno = 0


#*#################################################################################
#* Chequeo los valores mencionados 
#*#################################################################################


#* 680 aprobaron literatura y los datos se recolectaron en un diccionario
def suma_valores_diccionario(diccionario):
    suma = 0
    for elemento in diccionario.values():
        suma = suma + elemento
    return suma

suma_literatura = suma_valores_diccionario(diccio_literatura)
print(suma_literatura)

def suma_tuplasOListas(tuplaOLista):
    suma = 0
    for elemento in tuplaOLista:
        suma = suma + elemento
    return suma

#* 320 aprobaron biología y los datos se recolectaron en una tupla
suma_biologia = suma_tuplasOListas(tupla_biologia)
print(suma_biologia)

#* 490 opinaron sobre Educación
suma_matematica = suma_tuplasOListas(lista_matematica)
print(suma_matematica)


#!#################################################################################
#! Fin de control 
#!#################################################################################

#*#################################################################################
#* Convierto las estructuras a set
#*#################################################################################
def set_diccionario(diccionario):
    setDiccionario = set()
    for elemento in diccionario.values():
        setDiccionario.add(elemento)
    return setDiccionario

literatura = set_diccionario(diccio_literatura)
print(f'Total Literatura: >{literatura}')

#* También tengo que convertir tuplas y listas a set
matematica = set(lista_matematica)
print(f'Total Matematica: {matematica}')

#* Paso a set la tupla
biologia = set(tupla_biologia)
print(f'Total Biologia: {biologia}')

#!#################################################################################
#!  Fin de conversión de estructuras a set
#!#################################################################################

#*#################################################################################
#*  a) Cuántos aprobaron biología, matemática y literatura
#*#################################################################################

def unionABC(A, B, C):
    return (A & B & C)

aprobaronLasTres = unionABC(biologia,matematica,literatura)
print (f"Aprobaron las tres: {aprobaronLasTres}")

#*#################################################################################
#*  b) Cuántos aprobaron solo literatura y matemática?
#*#################################################################################
def soloDosGrupos(a,b,abc):
    return (a&b)-abc


soloLM = soloDosGrupos(literatura, matematica,aprobaronLasTres)
print(f"Aprobaron L y M: {soloLM}")

soloBM = soloDosGrupos(biologia,matematica,aprobaronLasTres)
print(f"Aprobaron B y M: {soloBM}")

soloBL = soloDosGrupos(biologia,literatura,aprobaronLasTres)
print(f"Aprobaron B y L: {soloBL}")

#*#################################################################################
#*  c) Cuantos aprobaron sólo literatura?
#*#################################################################################
def soloUNO(principal, a, b):
    return sum((principal - a) - b)

soloL = soloUNO(literatura, matematica, biologia)
print(f'Aprobaron solo literatura: {soloL}')

#*#################################################################################
#*  d) Cuántos aprobaron sólo biología?
#*#################################################################################
soloB = soloUNO(biologia,literatura, matematica)
print(f'Aprobaron solo biologia: {soloB}')

#*#################################################################################
#*  e) Cuántos aprobaron sólo matemática?
#*#################################################################################
soloM = soloUNO(matematica,biologia,literatura)
print(f'Aprobaron solo matematica: {soloM}')

#*#################################################################################
#*  f) Cuántos aprobaron 2 de los 3 exámenes?
#*#################################################################################
def dosDeTres(a,b,c):
    return sum(((a&b)|(a&c)|(b&c))-(a&b&c))

aprobaronDosDeTres = dosDeTres(matematica,literatura,biologia)
print(f'Aprobaron dos de tres: {aprobaronDosDeTres}')

#!#################################################################################
#! Fin de respuestas
#!#################################################################################


#*#################################################################################
#* Gráfico de resultados
#*#################################################################################

#* Ventana del gráfico

plt.figure('Primer parcial ')

#* Dibujo los diagramas con sus títulos
diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Literatura", "Matemática", "Biología"))

#* Establezco el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

#* Transfiero los resultados de las operaciones
diagram.get_label_by_id('100').set_text(soloL)
diagram.get_label_by_id('010').set_text(soloM)
diagram.get_label_by_id('001').set_text(soloB)
diagram.get_label_by_id('110').set_text(sum(soloLM))
diagram.get_label_by_id('011').set_text(sum(soloBM))
diagram.get_label_by_id('101').set_text(sum(soloBL))
diagram.get_label_by_id('111').set_text(sum(aprobaronLasTres))

#* Marco los contornos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

#* Agrego los datos universales y conjunto vacío
plt.text(-0.90, 0.67,
         f"Universal = {universal}",
         size=10)

plt.text(0.40, -0.5,
         f"Fuera\nde los\nconjuntos = {ninguno}",
         size=8)

#* Respondo las preguntas a,b,c,d,e y f
plt.text(-1.10, -0.20,
         s="Respuestas: ",
         size=8,
         ha="left",  # Alineación horizontal
         va="bottom",  # Alineación vertical
         bbox=dict(boxstyle="square",  # Tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.30,
         s="a) Aprobaron Biología, Matemática y Literatura = " + str(sum(aprobaronLasTres)),
         size=8,
         ha="left",  # Alineación horizontal
         va="bottom",  # Alineación vertical
         bbox=dict(boxstyle="square",  # Tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.40,
         s="b) Aprobaron sólo Literatura y Matemática = " + str(sum(soloLM)),
         size=8,
         ha="left",  # Alineación horizontal
         va="bottom",  # Alineación vertical
         bbox=dict(boxstyle="square",  # Tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.50,
         s="c) Aprobaron sólo Literatura = " + str(soloL),
         size=8,
         ha="left",  # Alineación horizontal
         va="bottom",  # Alineación vertical
         bbox=dict(boxstyle="square",  # Tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.60,
         s="d) Aprobaron sólo biología = " + str(soloB),
         size=8,
         ha="left",  # Alineación horizontal
         va="bottom",  # Alineación vertical
         bbox=dict(boxstyle="square",  #Ttipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.70,
         s="e) Aprobaron sólo matemática = " + str(soloM),
         size=8,
         ha="left",  # Alineación horizontal
         va="bottom",  # Alineación vertical
         bbox=dict(boxstyle="square",  # Tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.80,
         s="f) Aprobaron solo 2 de los 3 exámenes = " + str(aprobaronDosDeTres),
         size=8,
         ha="left",  # Alineación horizontal
         va="bottom",  # Alineación vertical
         bbox=dict(boxstyle="square",  # Tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

#* Recuadro
plt.axis('on')  

#* Título
plt.title("Encuestados")

#* Muestro el gráfico
plt.show()

#!#################################################################################
#! Fin de programa
#!#################################################################################