
cadena = input() #"neuquen"

i = 0
capicua = True
while i < (len(cadena)//2) and capicua:
    j = len(cadena) - i - 1
    j = -len(cadena) + i # alternativo
    capicua = capicua and (cadena[i] == cadena[j])
    i = i + 1

print(capicua)


#    print(f"{i} {j} {cadena[i]}")

#cadena == cadena[::-1]