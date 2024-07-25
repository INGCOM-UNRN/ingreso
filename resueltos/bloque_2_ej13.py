# 13. Escribir un programa 
#  que pida el ingreso de dos cadenas 
#   e indique si todos los caracteres 
#   de la primera están incluidos 
#   en la segunda


cadena_uno = "abcde"
cadena_dos = "abcdefg"

existe = False
cuenta = 0

for caracter in cadena_uno:
    for caracter_dos in cadena_dos:
        if caracter == caracter_dos:
            existe = True
    if existe:
        cuenta = cuenta + 1
    existe = False

print(cuenta, len(cadena_uno))
