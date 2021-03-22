#! /usr/bin/env python
# con /env variable del entorno

# espera salida ENTER
# raw_input()

# imprimir en pantalla del interprete (consola)
print
# solo print crea salto de linea
print('HOLA MUNDO')
print

#para imprimir triple linea, con comillas triples
triples = """primera linea
segunda linea
_____________"""
print(triples)


# tipos de datos numeros (y booleanos)
print("Tipos de datos:")
print
cadena = "quien siembra recoje"
entero = 23
decimales = 0.78
boolTrue = True
boolFalse = False

# tipo de dato Nulo, sin datos, vacio
None

# tipos de datos de Colecciones, un tipo, varios tipos..
tu = ("ROGER", "RABBIT")
lista = ["uno", 2, "tres", True, [1, 2]]
dicc = {"CONEJOS": "RABBIT"}
diccGrande = {"NombrePersona": "Li",
           "Apellidos": "Meng Yan",
           "Edad": "22"}
print(lista)
print(diccGrande)

# para imprimir los tipos de datos
print(type(cadena))
print(type(entero))
print(type(decimales))
print(type(boolTrue))
print(type(boolFalse))
print(type(None))
print(type(tu))
print(type(lista))
print(type(dicc))
print(type(diccGrande))
