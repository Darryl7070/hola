import pandas as pd

Trabajadores = pd.DataFrame(columns=("Nombre","Rut","Edad","Cargo","Contrato"))
documento = open("Proyecto1\\Personal\\Rut.txt")
Usuario = "Hola"
Usuario = documento.readline()

while Usuario != "":
    Arch = open(f"Proyecto1\Personal\{Usuario.strip("\n")}\Información")
    Datos = Arch.readline().split(",")
    Datos[-1] = int(Datos[-1].strip("\n"))
    Trabajadores.loc[len(Trabajadores)] = (Datos[0],Datos[1],Datos[2],Datos[3],Datos[4])
    Usuario = documento.readline()



print(Trabajadores)
Trabajadores.to_excel("Hola.xlsx")





