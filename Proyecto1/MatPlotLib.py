import pandas as pd 
import matplotlib.pyplot as plt
mes = ["1-Enero","2-Febrero","3-Marzo","4-Abril","5-Mayo","6-Junio","7-Julio","8-Agosto","9-Septiembre","10-Octubre","11-Noviembre","12-Diciembre"]
Ingresos = []
Index = []

i = int(input("Ingrese el año a graficar:"))
for x in range(12):
    Index.append(f"{mes[x]}")

for x in range(12):
    Arch = open(f"Proyecto1\IngresosMensuales\Año {i}\{mes[x]}\IngresosDelMes.txt")
    linea = Arch.readline()
    Ingresos.append(int(linea)*0.001)

Trabajadores = pd.DataFrame(columns=["Ingresos"])

for i in range(0,len(Ingresos)):
    Trabajadores.loc[Index[i]] = Ingresos[i]

total = Trabajadores.sum(axis=1)
plt.bar(total.index, total)
plt.show()