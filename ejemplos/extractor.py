import glob

archivos = glob.glob("./licenciatura/*.py")

alumnos = []

for nombre in archivos:
    with open(nombre, "r") as archivo:
        estu = archivo.readline()
        print(estu)
        alumnos.append(f"{archivo},{estu}")
        
with open("output.list", "w") as archivo:
    archivo.writelines(alumnos)
    

