# Análisis de inventario por sucursal

Proyecto académico para **Programación Computacional III – Segundo Cómputo**, Universidad Gerardo Barrios. La base de datos es ficticia y se utiliza únicamente con fines académicos.

## Integrantes

- Miguel Angel Herrera

## Contenido

- `datos.csv`: inventario simulado de 10 productos en las cinco sucursales (50 filas).
- `generar_inventario.py`: genera el CSV reproduciblemente usando un DataFrame de Pandas.
- `analisis_inventario.py`: inspección de estructura, tipos, estadísticas, faltantes y resúmenes con Pandas.
- `app.py`: interfaz de escritorio con PyQt5 y gráficos de Matplotlib.
- `informe_consultoria.pdf`: informe con el detalle del inventario por sucursal, hallazgos, conclusiones por variable y recomendaciones.
- `requirements.txt`: dependencias de Python.
- `.gitignore`: archivos temporales excluidos del control de versiones.

## Requisitos

Python 3.10 o superior y `pip`. La aplicación gráfica abre una ventana; en equipos sin escritorio puede ejecutarse el análisis de Pandas, pero no la ventana.

## Instalación

Desde la carpeta del proyecto, se recomienda crear un entorno virtual.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Windows (PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Sí, Pandas debe instalarse** en el entorno donde ejecuten el análisis o la aplicación. Se instala junto con Matplotlib y PyQt5 al ejecutar `pip install -r requirements.txt`.

## Ejecución

Analizar los datos en consola:

```bash
python analisis_inventario.py
```

Abrir el panel gráfico:

```bash
python app.py
```

Para volver a generar los datos sintéticos antes de ejecutar los otros programas:

```bash
python generar_inventario.py
```

La aplicación permite cambiar el gráfico entre valor y unidades por sucursal, unidades por categoría y valor por producto. `app.py` y `analisis_inventario.py` deben permanecer en la misma carpeta que `datos.csv`.

## Publicar en GitHub

Creen un repositorio vacío llamado `parcial-inventario-pc3` en su cuenta y sigan las instrucciones de GitHub para enlazar esta carpeta. Desde una terminal abierta en la carpeta del proyecto:

```bash
git init
git add .
git commit -m "Entrega de análisis de inventario"
git branch -M main
git remote add origin https://github.com/USUARIO/parcial-inventario-pc3.git
git push -u origin main
```

Reemplacen `USUARIO` por el nombre de la cuenta que creó el repositorio. Si el docente necesita revisar un repositorio privado, agréguenlo como colaborador; si no, confirmen primero si la entrega debe ser pública.

## Nota metodológica

El CSV contiene datos sintéticos, no cifras reales de la empresa. Se simularon los cinco locales solicitados y se calcularon estadísticas descriptivas para demostrar el flujo de análisis. Las decisiones comerciales del informe son recomendaciones ilustrativas y deben validarse con datos reales antes de aplicarse.
