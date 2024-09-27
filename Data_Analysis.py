#Análisis de Datos con Cruces de Datos
#Para realizar análisis de datos y cruces de datos, puedes utilizar bibliotecas como Pandas y NumPy. Aquí tienes un ejemplo básico:

import pandas as pd

# Cargar datos desde archivos CSV
df1 = pd.read_csv('archivo1.csv')
df2 = pd.read_csv('archivo2.csv')

# Realizar un cruce de datos (merge)
merged_df = pd.merge(df1, df2, on='id')

# Análisis básico
print(merged_df.describe())
