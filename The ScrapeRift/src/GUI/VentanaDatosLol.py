import sys
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QMessageBox,
    QLineEdit, QTableWidget, QTableWidgetItem,
)
from data.DataStorage import DataStorage



class VentanaDatosLoL(QWidget):
    """
    Ventana para mostrar los datos scrapeados de un campeón de LoL.
    """
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.inicializarUI()

    def inicializarUI(self):
        """Inicializa la interfaz de usuario."""
        self.setWindowTitle("Datos del Campeón de LoL")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.table = QTableWidget(self)
        self.table.setRowCount(1)
        self.table.setColumnCount(len(self.data.keys()))
        self.table.setHorizontalHeaderLabels(self.data.keys())
        layout.addWidget(self.table)

        for col, (key, value) in enumerate(self.data.items()):
            self.table.setItem(0, col, QTableWidgetItem(str(value) if value is not None else "N/A"))

        self.input_ruta = QLineEdit(self)
        self.input_ruta.setPlaceholderText(
            "Ingrese la ruta completa para guardar el archivo JSON "
            "(incluyendo el nombre del archivo)"
        )
        layout.addWidget(self.input_ruta)

        self.btn_guardar = QPushButton("Guardar Datos", self)
        self.btn_guardar.clicked.connect(self.guardar_datos)
        layout.addWidget(self.btn_guardar)

        self.setLayout(layout)

    def guardar_datos(self):
        """Guarda los datos en un archivo JSON."""
        file = self.input_ruta.text()
        if file:
            try:
                ds = DataStorage(self.data, "champion_data.json", file)
                ds.save_data(self.data)
                QMessageBox.information(self, "Guardar Datos", f"Datos guardados en {file}")
            except Exception as e:
                QMessageBox.critical(self, "Error al Guardar Datos", f"Error al guardar los datos: {e}")
        else:
            QMessageBox.warning(self, "Guardar Datos", "Por favor, ingrese una ruta válida.")

