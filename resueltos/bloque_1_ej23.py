# 23 Números primos

#  Escribir un programa que indique 
#   si un número ingresado es primos o no. 
#   Un número primo es un número entero 
#   mayor que 1 que tiene 
#   únicamente dos divisores 
#   positivos distintos: él mismo y el 1. 
# Por ejemplo; 7

for numero in range(100000):
    contador = 0
    
    for item in range(2, numero // 2):
        if numero % item == 0:
            print(f"{item} es divisor de {numero}")
            contador = contador + 1
    if contador == 0:
        print(f"el {numero=} es primo")
