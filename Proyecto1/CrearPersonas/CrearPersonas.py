import os as o
import random as rn

def Crear_Rut():
    digitos1 = rn.randint(1,22)
    digitos2 = rn.randint(100,999)
    digitos3 = rn.randint(100,999)
    digito = rn.randint(0,9)
    if digito == 0:
        digito = "k"
    Rut = (f"{digitos1}.{digitos2}.{digitos3}-{digito}")
    return Rut

def Crear_Nombre():
    documento = open("Proyecto1\\CrearPersonas\\Nombres.txt")
    lista = []
    for i in range(100):
        linea = documento.readline()
        linea = linea.strip("\n")
        lista.append(linea)
    Nombre = lista[rn.randint(0,99)]
    documento.close()
    return Nombre

def Crear_Apellido():
    documento = open("Proyecto1\\CrearPersonas\\Apellidos.txt")
    lista = []
    for i in range(100):
        linea = documento.readline()
        linea = linea.strip("\n")
        lista.append(linea)
    Apellido = lista[rn.randint(0,99)]
    documento.close()
    return Apellido

def Crear_Cargo():
    documento = open("Proyecto1\\CrearPersonas\\Cargo.txt")
    lista = []
    for i in range(15):
        linea = documento.readline()
        linea = linea.strip("\n")
        lista.append(linea)
    Cargo = lista[rn.randint(0,14)]
    documento.close()
    return Cargo

def Carpetas_Personal(NombreTrabajador,Rut):
    o.mkdir(f"Proyecto1\Personal\{Rut}")
    Documento = open(f"Proyecto1\Personal\{Rut}\Información","x")
    Documento = open(f"Proyecto1\Personal\{Rut}\Información","w")
    Nombre=(f"{NombreTrabajador} {Crear_Apellido()}")
    Edad = rn.randint(20,80)
    Cargo=Crear_Cargo()
    Contrato= rn.randint(5,10)
    Documento.write(f"{Nombre},{Rut},{Edad},{Cargo},{Contrato}\n")
    print("Usuario creado con exito.")

documento = open("Proyecto1\\Personal\\Rut.txt")
linea = documento.readline()
print(linea)
Lista = []
while linea != "":
    Lista.append(linea)
    linea = documento.readline().strip("\n")
    linea.strip("\n")

documento = open("Proyecto1\\Personal\\Rut.txt","a")

for i in range(int(input("Ingrese una cantidad de usuarios a crear:"))):
    Rut = Crear_Rut()
    try:
        Lista.index(Rut)
        print("El usuario ya existe.")
        i -= 1
    except:
        Nombre = Crear_Nombre()
        Carpetas_Personal(Nombre,Rut)
        documento.write(f"{Rut}\n")
        
    
documento.close()


