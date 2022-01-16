# Entregar cada ejercicio en un archivo distinto con el nombre EJFUNN.py, donde NN es 01, 02, 03, según corresponda al número de ejercicio.
# 01. Dada una cadena, devolver una lista dividiendo la cadena en subcadenas de dos caracteres. Si tiene un nro impar de caracteres, completar el último par con guión bajo. "Un ejemplar"->["Un", " e", "je", "mp","la", "r_"]

# def trozear_cadena(cadena):
#     for i in cadena:
        
#         print(i)

# trozear_cadena('Un ejemplar')


# 02. Dada una cadena, devolver la cantidad de . que tiene al comienzo la cadena. ".....casa"->5.



# 03. Dado un conjunto de números, y un número aparte, devolver cuál es el número del conjunto más cercano al dado. {4,6,12,15,22}, 9->6 (podría haber devuelto 12 también)

from heapq import nsmallest

def cercano(numero_a_consultar, ingrese_posiciones_a_buscar_en_la_lista, ingrese_diccionario):
    dictionary = ingrese_diccionario
    print(nsmallest(ingrese_posiciones_a_buscar_en_la_lista, dictionary, key=lambda x:abs(x-numero_a_consultar)))

diccionario_numeros={4,6,12,15,22}

cercano(9,2,diccionario_numeros)



# 04. Dada una cadena, devolverla en formato "correcto": comenzando con mayúsculas y finalizando con un . "esto es ejemplo"->"Esto es ejemplo."
def correcto(cadena):
    print(cadena.capitalize()+'.')

correcto('esto es un ejemplo')

# 05. Dado una cadena, devolver la cadena con cada palabra invertida. La cadena tiene sólo caracteres alfanuméricos y espacios. "Esto es ejemplo"->"otsE se olpmeje"

def reverse(cadena):
    return ' '.join(list(map(lambda x: x[::-1], cadena.split())))

print(reverse("Hola como estas"))


import re

pat = re.compile("\w+")
print(pat.findall("¡Hola, Mundo!"))


def invert(m):
    return m.group(0)[::-1]

resultado = pat.sub(invert, "¡Hola, Mundo!")

print(resultado)


# 06. Dada una cadena, devolver la cantidad de dígitos que hay en la cadena. "Acá tenemos 2 dígitos"->1

""" def contardigitos(cadena):
    digitos=0
    for c in cadena:
        if c.isdigit():
            digitos+=1
        else: c.isalpha()
        pass
    return digitos

texto=input("Digite un texto: ")
resultado=contardigitos(texto)
print(f"Aca tenemos: {resultado}") """

# 07. Dado un número M y varios diccionarios de la forma {"prod": "manzana", "pre":5.5}, devolver una lista con los M productos más caros. 2, {"prod":"pan", "pre": 100}, {"prod":"arroz", "pre": 50}, {"prod":"leche", "pre": 90}, {"prod":"carne", "pre": 300}->[{"prod":"pan", "pre": 100}, {"prod":"carne", "pre": 300}]
from collections import OrderedDict
import operator

def mayores_precios(cantidad_producto_mostrar, lista):

    diccionario_productos=lista
    ordenados = sorted(diccionario_productos, key=lambda precio : precio['precio'],reverse=True)
    
    conteo=0
    for productos in ordenados:
        if conteo < cantidad_producto_mostrar:
            print(productos)
            conteo+=1
        else:
            break



diccionario_productos =[
        {"prod":"pan", "precio": 100},
        {"prod":"arroz", "precio": 50},
        {"prod":"leche", "precio": 90},
        {"prod":"carne", "precio": 300}
        ]

mayores_precios(2, diccionario_productos)


# 08. Dadas una cadena C1, y una cadena C2, devolver la posición de la SEGUNDA vez que aparece C2 dentro de C1. Si no aparece o lo hace una sola vez, devolver None. "Esto es una estatua", "st"->13

def encontrar_todas(cadena, cadena1):
	posiciones = []
	posicion = 0
	
	while posicion != -1:
		posicion = cadena.find(cadena1,posicion)
		if posicion != -1:
			posiciones.append(posicion)
			posicion += 1

	return posiciones


cadena = 'Esto es una estatua'
cadena1 = 'ma'

posiciones = encontrar_todas(cadena, cadena1)

print('Posiciones:', posiciones)