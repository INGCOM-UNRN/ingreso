numero = 125
n = numero
suma = 0
while n>0:
    digito = n % 10
    cociente = n // 10
    suma = suma + digito
    n = cociente
    print(f"{n=} {suma=} {digito=}")
print(f"la suma de los digitos de {numero} es {suma}")
print(suma == 1 + 2 + 5)
