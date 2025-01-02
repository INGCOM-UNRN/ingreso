cadena = "neuq3uen" # reemplazar por un input
i = 0
capicua = True
largo = len(cadena)
while i < (largo // 2) and capicua:
	j = largo - i - 1
	#j = -len(cadena) + i # alternativo
	capicua = capicua and (cadena[i] == cadena[j])
	i = i + 1

if not capicua:
    print(cadena)
    print(("-"*(i-1))+"^")
else:
    print(f"Es capicua")




#    print(f"{i} {j} {cadena[i]}")

#cadena == cadena[::-1]