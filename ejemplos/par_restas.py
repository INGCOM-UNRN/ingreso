# Ingreso Ingeniería en Computación - UNRN Andina
# Martín René Vilugrón
# mrvilugron@unrn.edu.ar
# Ejercicios Python I - 17:
# Consigna: Escribir un programa que pida el ingreso de un número y determine 
#           si el número es par o impar.
# PRE: el número a evaluar debe ser un número natural o cero.
#      (de otra forma las restas no llegarian a un resultado)
#      el valor ingresado no será modificado por el programa
# POST: el resultado debe ser un valor lógico que indique con True si es par



numero = int(input("Ingrese un número natural"))

assert isinstance(numero, int), "El número debe ser entero"
assert numero >= 0, "Número debe ser natural o cero"

i = numero

while i > 1:
    i = i - 2

es_par = i == 0

assert isinstance(es_par, bool), "el resultado debe ser un valor lógico"

print (f"El número {numero} es ", end="")
if es_par:
    print("par")
else:
    print("impar")
