"""Genera el CSV académico de inventario usando Pandas."""
from pathlib import Path
import pandas as pd

RUTA_CSV = Path(__file__).with_name("datos.csv")
SUCURSALES = ["San Salvador", "Santa Ana", "San Miguel", "La Libertad", "Sonsonate"]
PRODUCTOS = [
    ("Laptop Lenovo IdeaPad", "Tecnología", 549.99, "TecnoDistribuidora"),
    ("Mouse inalámbrico", "Accesorios", 14.50, "CompuCentro"),
    ("Teclado mecánico", "Accesorios", 39.99, "CompuCentro"),
    ("Monitor 24 pulgadas", "Tecnología", 159.00, "TecnoDistribuidora"),
    ("Audífonos Bluetooth", "Audio", 32.75, "ElectroHogar"),
    ("Impresora multifuncional", "Oficina", 129.99, "Papelería Central"),
    ("Memoria USB 64 GB", "Almacenamiento", 9.90, "TecnoDistribuidora"),
    ("Disco SSD 1 TB", "Almacenamiento", 84.50, "CompuCentro"),
    ("Bocina portátil", "Audio", 27.99, "ElectroHogar"),
    ("Silla ergonómica", "Oficina", 189.00, "Muebles SV"),
]
EXISTENCIAS_BASE = [12, 55, 22, 15, 28, 10, 70, 18, 24, 8]
FACTORES_SUCURSAL = [1.35, 0.95, 1.10, 0.80, 0.90]

registros = []
for indice_sucursal, sucursal in enumerate(SUCURSALES):
    for indice_producto, (producto, categoria, precio, proveedor) in enumerate(PRODUCTOS):
        variacion = ((indice_sucursal * 7 + indice_producto * 3) % 9) - 4
        cantidad = max(
            2,
            round(EXISTENCIAS_BASE[indice_producto] * FACTORES_SUCURSAL[indice_sucursal]) + variacion,
        )
        registros.append({
            "Sucursal": sucursal,
            "Producto": producto,
            "Categoria": categoria,
            "Cantidad": cantidad,
            "Precio_Unitario_USD": precio,
            "Proveedor": proveedor,
        })

df = pd.DataFrame(registros)
df.to_csv(RUTA_CSV, index=False, encoding="utf-8-sig")
print(f"CSV generado: {RUTA_CSV} ({len(df)} filas, {len(df.columns)} columnas)")
