def leer_archivos (Archivo):
    Documento = open(f"{Archivo}.txt")
    linea = Documento.readline().split(",")
    return linea
