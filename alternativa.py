#Librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Cargar datos
data = pd.read_csv('Datos.csv')

#Limpieza de datos

#Eliminar filas con valores nulos
data.dropna(inplace=True)

#Eliminar duplicados
data.drop_duplicates(inplace=True)

