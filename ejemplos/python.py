# Decisión simple

numero = int(input("Ingresá un número entero"))
if numero > 10:
    print("numero es")
    print("má que dié")


# Decisión basica
print("antes")
if n > 10:
    print("es mayor a 10")
else:
    print("no es mayor a 10")
print("despues")


# Secuencia en Decisiones I
print("antes")
if n > 10:
    print("mayor que 10")
elif n > 20:
    print("mayor que 20")
elif n > 30:
    print("mayor que 30")
print("despues")


# Secuencia en Decisiones II
n = int(input("Ingresá un numero para clasificar"))
print("antes")
if n > 30:
    print("mayor que 30")
elif n > 20:
    print("mayor que 20")
elif n > 10:
    print("mayor que 10")
print("despues")



# Lazos automáticos

numero = int(input("Ingresá un número entero"))
for i in range(n):
    print(f"i vale {i}")

# Lazos automáticos sobre cadenas
msg = input("Ingresá un mensaje")
for c in msg:
    print(f"{c}")

# Decreciente

n = 10
while n > 0:
    print(f"n vale {n}")
    n = n - 1
print(f"n vale {n}")


# Decreciente alternativo
n = 10
while n > 0:
    n = n - 1
    print(f"n vale {n}")
print(f"n vale {n}")

# Creciente

n = 10
i = 0
while i < n:
    print(f"i vale {i}")
    i = i + 1
print(f"n vale {i}")

# por bandera

n = 10
bandera = True
while bandera:
    print(f"n vale {n}")
    n = n - 1
    if n > 0:
        bandera = False


# Suma de dígitos
numero = 125
suma = 0
while numero >0:
  digito = numero  % 10
  cociente = numero // 10
  suma = suma + digito
  numero  = cociente
print(suma)
print(suma == 1 + 2 + 5)

# Enumeración
msg = input("Ingresá un mensaje")
for i, c in enumerate(msg):
    print(f"el caracter {i} es {c}")
    
# Rangos avanzados
desde = int(input("Ingresá un número entero"))
hasta = int(input("Ingresá un número entero"))
paso = int(input("Ingresá un número entero"))
for i in range(desde,hasta,paso):
    print(f"i vale {i}")
    

