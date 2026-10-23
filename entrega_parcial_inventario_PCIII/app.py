
from pathlib import Path
import sys

import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QComboBox, QLabel, QMainWindow, QMessageBox,
    QVBoxLayout, QWidget,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

CSV_PATH = Path(__file__).with_name("datos.csv")


class InventoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Panel de inventario por sucursal")
        self.resize(1000, 680)
        self.df = self.load_inventory()

        central = QWidget()
        layout = QVBoxLayout(central)
        self.setCentralWidget(central)

        title = QLabel("INVENTARIO COMERCIAL | EL SALVADOR")
        title.setStyleSheet("font-size: 22px; font-weight: 700; color: #153b68; padding: 8px;")
        layout.addWidget(title)

        description = QLabel(
            f"{len(self.df)} registros · {self.df['Sucursal'].nunique()} sucursales · "
            f"{self.df['Producto'].nunique()} productos"
        )
        description.setStyleSheet("font-size: 13px; color: #566477; padding: 0 8px 8px 8px;")
        layout.addWidget(description)

        self.selector = QComboBox()
        self.selector.addItems([
            "Valor del inventario por sucursal",
            "Unidades en existencia por sucursal",
            "Unidades en existencia por categoría",
            "Valor del inventario por producto",
        ])
        self.selector.currentIndexChanged.connect(self.draw_chart)
        layout.addWidget(self.selector)

        self.figure = Figure(figsize=(9, 5), tight_layout=True)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas, stretch=1)
        self.draw_chart()

    @staticmethod
    def load_inventory():
        if not CSV_PATH.exists():
            raise FileNotFoundError(f"No se encontró el archivo: {CSV_PATH}")
        data = pd.read_csv(CSV_PATH)
        required = {"Sucursal", "Producto", "Categoria", "Cantidad", "Precio_Unitario_USD"}
        missing = required.difference(data.columns)
        if missing:
            raise ValueError("Faltan columnas requeridas: " + ", ".join(sorted(missing)))
        data["Valor_Inventario_USD"] = data["Cantidad"] * data["Precio_Unitario_USD"]
        return data

    def draw_chart(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        choice = self.selector.currentIndex()

        if choice == 0:
            summary = self.df.groupby("Sucursal")["Valor_Inventario_USD"].sum().sort_values(ascending=False)
            ax.bar(summary.index, summary.values, color="#3478b8")
            ax.set_title("Valor estimado del inventario por sucursal (USD)")
            ax.set_ylabel("Dólares (USD)")
            self.add_value_labels(ax, "${:,.0f}")
        elif choice == 1:
            summary = self.df.groupby("Sucursal")["Cantidad"].sum().sort_values(ascending=False)
            ax.bar(summary.index, summary.values, color="#2a9d8f")
            ax.set_title("Unidades en existencia por sucursal")
            ax.set_ylabel("Unidades")
            self.add_value_labels(ax, "{:,.0f}")
        elif choice == 2:
            summary = self.df.groupby("Categoria")["Cantidad"].sum().sort_values(ascending=False)
            ax.bar(summary.index, summary.values, color="#e09f3e")
            ax.set_title("Unidades en existencia por categoría")
            ax.set_ylabel("Unidades")
            self.add_value_labels(ax, "{:,.0f}")
        else:
            summary = self.df.groupby("Producto")["Valor_Inventario_USD"].sum().sort_values()
            ax.barh(summary.index, summary.values, color="#6b6ecf")
            ax.set_title("Valor estimado del inventario por producto (USD)")
            ax.set_xlabel("Dólares (USD)")
            ax.grid(axis="x", alpha=0.2)
            for bar, value in zip(ax.patches, summary.values):
                ax.text(value, bar.get_y() + bar.get_height() / 2, f" ${value:,.0f}", va="center", fontsize=8)

        if choice < 3:
            ax.tick_params(axis="x", rotation=18)
            ax.grid(axis="y", alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
        self.figure.tight_layout()
        self.canvas.draw_idle()

    @staticmethod
    def add_value_labels(ax, fmt):
        for bar in ax.patches:
            height = bar.get_height()
            ax.annotate(fmt.format(height), (bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 4), textcoords="offset points", ha="center", fontsize=8)


def main():
    app = QApplication(sys.argv)
    try:
        window = InventoryWindow()
    except Exception as exc:
        QMessageBox.critical(None, "No se pudo cargar el inventario", str(exc))
        return 1
    window.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
