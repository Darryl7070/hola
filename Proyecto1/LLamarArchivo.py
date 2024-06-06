import os as o

def llamar_archivo(NombreTrabajador):
    if o.path.exists(f"Proyecto1\Personal\{NombreTrabajador}"):
        Nombre = True
    else:
        print("No se encontró el usuario")
        Nombre = False
    return Nombre

llamar_archivo("Luis")