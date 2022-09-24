"""
En una zona del país, se realizó una encuesta de opinión a 1000 personas sobre 3 (tres)
categorías: Economía, Educación y Seguridad, y otras sub-categorías especificadas
sólo para Economía. Los datos se recolectaron en las siguientes estructuras:

# 680 opinaron sobre Ecomomía.
Economia = {"Gasto_público": 40, "Impuestos": 118, "Política_y_gobierno": 50, "Deuda_externa": 95,
"Privilegios": 56, "Corrupción":  131, "Obra_pública": 103, "Planes": 87}
# 320 opinaron sobre Seguridad.
Seguridad = (40, 50, 60, 75, 34, 61)
# 490 opinaron sobre Educación
Educacion = [34, 40, 61, 75, 87, 90, 103]
   
En relación a los datos obtenidos:
    1) realizar las operaciones correspondientes
    2) realizar el gráfico en networkx
    3) Responder en el gráfico las siguientes preguntas:
        a. cuántos opinaron sobre Seguridad, Educación y Economía.
        b. cuántos opinaron sobre sólo Economía y Educación?
        c. cuántos opinaron sobre sólo Economía?
        d. cuántos opinaron sobre solo Seguridad?
        e. cuántos opinaron sobre sólo Educación?
        f. cuántos opinaron sobre 2 de las 3 categorías?
"""

from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles


lista_educacion = [34, 40, 61, 75, 87, 90, 103]
tupla_seguridad = (40, 50, 60, 75, 34, 61)
diccio_economia = {"Gasto_publico": 40, "Impuestos": 118, "Politica_y_gobierno": 50, "Deuda_externa": 95,
"Privilegios": 56, "Corrupcion":  131, "Obra_publica": 103, "Planes": 87}

print("HolaMundo")


#* Definir
universal = 1000
ninguno = 0


#*#################################################################################
#* Controlo los valores mencionados 
#*#################################################################################


#* 680 opinaron sobre Ecomomía
def suma_economia(diccio_economia):
    suma = 0
    for elemento in diccio_economia.values():
        suma = suma + elemento
    return suma

economia = suma_economia(diccio_economia)
print(economia)
def suma_tuplasOListas(tuplaOLista):
    suma = 0
    for elemento in tuplaOLista:
        suma = suma + elemento
    return suma

#* 320 opinaron sobre Seguridad.
seguridad = suma_tuplasOListas(tupla_seguridad)
print(seguridad)

#* 490 opinaron sobre Educación
educacion = suma_tuplasOListas(lista_educacion)
print(educacion)


#!#################################################################################
#! Se pueden reemplazar 2 ó más funciones por sólo una?. En caso afirmativo
#! reemplazarlas.
#! Cierre de control 
#!#################################################################################

#*#################################################################################
#* Convierto las estructuras a set (a resolver)
#*#################################################################################

def set_economia(diccio_economia):
    economia = set()
    for elemento in diccio_economia.values():
        economia.add(elemento)
    return economia

economia = set_economia(diccio_economia)
print(f'-_->{economia}')


#* También tengo que convertir tuplas y listas a set
#* paso a set la lista
educacion = set(lista_educacion)
print(educacion)


#* Paso a set la tupla
seguridad = set(tupla_seguridad)
print(seguridad)


#!#################################################################################
#!  cierre de conversión de estructuras
#!#################################################################################

#*#################################################################################
#* Los siguientes datos se facilitan, sólo hay que hacer las operaciones utilizando
#* funciones y controlar que el resultado sea el dado
#*#################################################################################


def soloDosGrupos(a,b,abc):
    return (a&b)-abc


#* Opniaron de los 3 temas
def economia_educacion_seguridad(f, s, t):
    return (f & t & s)


losTresGrupos = economia_educacion_seguridad(economia,educacion,seguridad)
print (losTresGrupos)



# Opinaron de economía y seguridad
soloECS = soloDosGrupos(economia, seguridad,losTresGrupos)
print(soloECS)


# Opinaron de seguridad y educacion
soloEDS = soloDosGrupos(educacion,seguridad,losTresGrupos)
print(soloEDS)



# Opinaron de economía y educacion
soloEDEC = soloDosGrupos(educacion,economia,losTresGrupos)
print(soloEDEC)

#!#################################################################################
#! Se pueden reemplazar 2 ó más funciones por sólo una?. En caso afirmativo
#! reemplazarlas.
#! Cierre de operaciones con resultados dados
#!#################################################################################

#*#################################################################################
#* Funciones y cálculos a resolver 
#*#################################################################################


#* Opinaron solo de un tema
def soloUNO(principal, a, b):
    return (principal - a) - b



#* Solo economía
soloEC = soloUNO(economia,seguridad,educacion)
print(soloEC)



#* Solo educación
soloED = soloUNO(educacion,economia,seguridad)
print(soloED)



#* Solo seguridad
soloS = soloUNO(seguridad,economia,educacion)
print(soloS)

#* "Opinaron de economía o seguridad"
#* para responder la pregunta hay que sumar los elementos del 
#* resultado de la operación entre conjuntos
def A_O_B(a, b):
    suma = 0
    a_o_b = ((a - b) | a)
    for elemento in a_o_b:
        suma = suma + elemento
    return suma

economia_o_seguridad = A_O_B(economia, seguridad)
print(economia_o_seguridad)


#!#################################################################################
#! Se pueden reemplazar 2 ó más funciones por sólo una?. En caso afirmativo
#! reemplazarlas.
#! Fin de Funciones y cálculos a resolver 
#!#################################################################################


#*#################################################################################
#* Gráfico de resultados
#*#################################################################################
#* Preparamos la ventana del gráfico
plt.figure('Primer parcial ')

#* Dibujamos los diagramas
diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Economia", "Seguridad", "Educacion"))

# establecemos el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text(sum(soloEC))
diagram.get_label_by_id('010').set_text(sum(soloED))
diagram.get_label_by_id('001').set_text(sum(soloS))
diagram.get_label_by_id('110').set_text(sum(soloEDEC))
diagram.get_label_by_id('011').set_text(sum(soloEDS))
diagram.get_label_by_id('101').set_text(sum(soloECS))
diagram.get_label_by_id('111').set_text(sum(losTresGrupos))

# marcamos los contornos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

# agregamos más datos aclaratorios al gráfico
plt.text(-0.90, 0.67,      # Texto y cantidad universal
         f"Universal = {universal}",
         size=10)

plt.text(0.40, -0.5,      # Texto fuera del conjunto
         f"Fuera\nde los\nconjuntos = {ninguno}",
         size=8)

# Respondemos las preguntas
plt.text(-1.10, -0.20,
         s="Respuestas solicitadas: ",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.30,
         s="Respondieorn solo sobre Seguridad = " + str(sum(soloS)),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.40,
         s="Respondieorn solo sobre Economía =" + str(sum(soloEC)),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.50,
         s="Respondieorn solo sobre Educación = " + str(sum(soloED)),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.60,
         s="Respondieorn sobre Economía o Seguridad = = " + str(economia_o_seguridad),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.axis('on')  # Recuadro
plt.title("Encuestados")
plt.show()
##################################################################################
# Fin de programa
##################################################################################
