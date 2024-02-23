# Escribir un programa que imprima un arbolito


alto = int(input("cual es la altura del arbolito a plantar"))

for i in range(alto):
    print(" "*(alto-i-1)+"*"*i+"*"+"*"*i)

for i in range((alto//4)+1):
    print(("|"*((alto//2))).center(alto*2))


