import random as rn
import os as o
import pandas as pd
import openpyxl as op
from openpyxl import load_workbook

def Elementos_Comprados():
    elementos = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(elementos)):
        elementos[i] = rn.randint(80,100)

    return elementos

def Crear_Exel(año):
    exel = op.Workbook()
    exel.save(f"Proyecto1\GastosMensuales\Año {año}\Gastos año {año}.xlsx")

def Generar_Gastos():
    
    mes = ["1-Enero","2-Febrero","3-Marzo","4-Abril","5-Mayo","6-Junio","7-Julio","8-Agosto","9-Septiembre","10-Octubre","11-Noviembre","12-Diciembre"]
    elementos = ["Insumos","Transporte","Pagos Empresas Externos","Alojamiento","EPP","Colaciones","Gastos Basicos (Agua, Luz, Etc.)","Maquinaria","Salarios","Gastos Legales"]
    sensibilidades = [200,50,100,50,20,30,150,100,200,50]
    MontoMensual = 0
    for i in range(2000,2025):
        lista=[]
        if not o.path.exists(f"Proyecto1\GastosMensuales\Año {i}"):
            o.mkdir(f"Proyecto1\GastosMensuales\Año {i}")
        Crear_Exel(i)
        for x in range(12):
            if not o.path.exists(f"Proyecto1\GastosMensuales\Año {i}\{mes[x]}"):
                o.mkdir(f"Proyecto1\GastosMensuales\Año {i}\{mes[x]}")
                Archivo = open(f"Proyecto1\GastosMensuales\Año {i}\{mes[x]}\GastosDelMes.txt","x")

            Archivo = open(f"Proyecto1\GastosMensuales\Año {i}\{mes[x]}\GastosDelMes.txt","a")
            MontoMensual = Elementos_Comprados()
            for z in range(len(MontoMensual)):
                MontoMensual = Elementos_Comprados()
                for y in range(10):
                    MontoMensual[y] *= sensibilidades[y]
                Archivo.write(f"{elementos[z]}: {str(MontoMensual[z])}\n")
            lista.append(MontoMensual)

        Df = pd.DataFrame(lista,columns=elementos,index=mes)
        Df.to_excel(fr"Proyecto1\GastosMensuales\Año {i}\Gastos año {i}.xlsx")

        


Generar_Gastos()
