# 18 Comparación de 4 variables
#  Escribir un programa que pida 
#  el ingreso de 4 valores e 
#  indique cuál es el menor de todos ellos.


uno = int(input("numero 1"))
dos = int(input("numero 1"))
tres = int(input("numero 1"))
cuatro = int(input("numero 1"))

if (uno < dos) and (uno < tres) and (uno < cuatro):
    print(uno, "es el menor")
    
    
    
menor = 0

contador = 1

print("Este programa indica que numero de los")
print("cuatro ingresados es menor.")

while contador < 5:
    
    numero = int(input(f"ingresa el {contador} numero: "))
    if contador == 1:
        menor = numero
    if numero < menor:
        menor = numero
    contador = contador + 1
    
    
print(f"el menor es {menor}")




menor = 0

lista = list()
contador = 1

print("Este programa indica que numero de los")
print("cuatro ingresados es menor.")

while contador < 5:
    numero = int(input(f"ingresa el {contador} numero: "))
    lista.append(numero)
    
    contador = contador + 1
    
lista.sort()
menor = lista[0]

print(f"el menor es {menor}")






menor = 0

lista = list()
contador = 1

print("Este programa indica que numero de los")
print("cuatro ingresados es menor.")

while contador < 5:
    numero = int(input(f"ingresa el {contador} numero: "))
    lista.append(numero)
    
    contador = contador + 1
    
lista.sort()
menor = min(lista)
### o
menor = lista[0]


print(f"el menor es {menor}")



