import pandas as pd
Df = {
    "Hola" : [1,2,3,4,5,6],
    "XD" : [6,5,4,3,2,1]
}
Df = pd.DataFrame(Df)

Df.to_excel(f"Proyecto1\GastosMensuales\Año 2000\Gastos año 2000.xlsx")