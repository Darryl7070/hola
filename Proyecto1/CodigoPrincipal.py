import os as o

def Carpetas_Personal(NombreTrabajador):

    if not o.path.exists(f"Proyecto1\Personal\{NombreTrabajador}"):
        o.mkdir(f"Proyecto1\Personal\{NombreTrabajador}")
        Documento = open(f"Proyecto1\Personal\{NombreTrabajador}\Información","x")
        Documento = open(f"Proyecto1\Personal\{NombreTrabajador}\Información","w")
        Nombre=input("Ingrese su nombre completo:")
        Rut=input("Ingrese su rut(Con el formato xx.xxx.xxx-x):")
        Edad=input("Ingrese su edad:")
        Cargo=input("Ingrese el cargo:")
        Contrato=input("Ingrese la duración de su contrato:")
        Documento.write(f"{Nombre},{Rut},{Edad},{Cargo},{Contrato}\n")
        print("Usuario creado con exito.")
    else:
        print("El usuario ya existe.")

def llamar_archivo(NombreTrabajador):
    if o.path.exists(f"Proyecto1\Personal\{NombreTrabajador}"):
        Nombre = True
    else:
        print("No se encontró el usuario")
        Nombre = False
    return Nombre

def leer_archivos (Archivo):
    Documento = open(f"{Archivo}.txt")
    linea = Documento.readline().split(",")
    return linea

