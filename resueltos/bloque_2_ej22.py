#22 Escribir una función que dada una cadena de
#caracteres, devuelva la primera letra de cada
#palabra.


cadena = " Universal Serial Bus     "

sigla = ""
sgla = ""
for palabra in cadena.split(" "):
    if len(palabra) > 0:
        sgla = sgla + palabra[0]

print(sgla)

for item in cadena:
    if item.isupper():
        sigla = sigla + item

s = cadena[0]
for posicion, item in enumerate(cadena):
    if item == " " and (posicion + 1) != len(cadena):
        s = s + cadena[posicion+1]

print(f"{cadena=}, {s=}")

#print(f"{cadena=}, {sigla=}")
