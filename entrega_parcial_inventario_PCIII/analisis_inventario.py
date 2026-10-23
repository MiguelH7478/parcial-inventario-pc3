from pathlib import Path
import pandas as pd

# El archivo CSV debe estar en la misma carpeta que este script.
RUTA_CSV = Path(__file__).with_name('datos.csv')
df = pd.read_csv(RUTA_CSV)

# Variable derivada para estimar el valor monetario de las existencias.
df['Valor_Inventario_USD'] = df['Cantidad'] * df['Precio_Unitario_USD']

print('=== MUESTRA DE REGISTROS ===')
print(df.head())

print('\n=== ESTRUCTURA Y TIPOS DE DATOS ===')
df.info()

print('\n=== ESTADÍSTICAS DE COLUMNAS NUMÉRICAS ===')
print(df.describe().round(2))

print('\n=== VALORES FALTANTES POR COLUMNA ===')
print(df.isna().sum())

print('\n=== CANTIDAD DE REGISTROS POR SUCURSAL ===')
print(df['Sucursal'].value_counts().sort_index())

print('\n=== EXISTENCIAS Y VALOR DEL INVENTARIO POR SUCURSAL ===')
por_sucursal = df.groupby('Sucursal').agg(
    Productos=('Producto', 'count'),
    Unidades=('Cantidad', 'sum'),
    Valor_USD=('Valor_Inventario_USD', 'sum'),
).sort_values('Valor_USD', ascending=False)
print(por_sucursal.round(2))

print('\n=== UNIDADES POR CATEGORÍA ===')
print(df.groupby('Categoria')['Cantidad'].sum().sort_values(ascending=False))

print('\n=== PRODUCTOS CON MENOS EXISTENCIAS TOTALES ===')
print(df.groupby('Producto')['Cantidad'].sum().sort_values().head(5))
