# Problema #1
#Problema 1:
# Se solicita al usuario que ingrese un número entero positivo 
# y calcule la cantidad de digitos 5 que contiene el número ingresado.



# Este ejemplo, que esta desarrollado con todo el tiempo, muestra la ubicación de
#  los dígitos buscados.
# Esta es una de las varias versiones posibles de este ejercicio.

#numero = input("ingrese un número entero positivo")
numero = "65656656566776765"

assert int(numero) > 0, "Hay dos cosas juntas aca; si es un número y si es positivo"

if len(numero)>9:
    espacios = 2
else:
    espacios = 1

contador = 0
linea_uno = ""
linea_dos = ""
linea_tre = ""
for posicion, caracter in enumerate(numero):
    posicion_real = posicion + 1
    linea_uno = linea_uno + f"{caracter}" + " " * espacios
    
    espacios_real = (len(str(posicion_real)) // 2)

    linea_dos = linea_dos + f"{posicion_real}" + " " * (espacios - espacios_real)
    
    if caracter == '5':
        contador = contador + 1
        linea_tre = linea_tre + "X" + " " * espacios
    else:
        linea_tre = linea_tre + " " * (espacios + 1)
        
print("para el número")
print(f"{numero}:")

print(linea_uno)
print(linea_dos)
print(linea_tre)

print(f"el dígito 5 aparece {contador} veces")

