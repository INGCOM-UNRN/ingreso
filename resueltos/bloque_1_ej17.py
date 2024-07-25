#17 Serie de dos
# Escribir un programa que pida el ingreso de un
#  número entero que indica la cantidad de
#  veces a sumar una serie del siguiente tipo
#  Si el número es 5, la serie sería:
#  5⇒2+22+222+2222+22222=24690


veces = 5
suma = 0

for item in range(1, veces+1):
    cadena = "2" * item
    print(f"vuelta {item}, {cadena=}")
    suma = suma + int("2" * item)    
    
print(suma)



#17 Serie de dos
# Escribir un programa que pida el ingreso de un
#  número entero que indica la cantidad de
#  veces a sumar una serie del siguiente tipo
#  Si el número es 5, la serie sería:
#  5⇒2+22+222+2222+22222=24690


veces = 5

contador = 0
actual = 0
suma = 0

while contador < veces:
    numero =  7 * (10 ** contador)
    actual = actual + numero
    suma = suma + actual
    contador = contador + 1
    
    print(f"{contador=}, {actual=}, {suma=}")

print(suma)
