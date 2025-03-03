import sys
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QMessageBox,
    QLineEdit, QTableWidget, QTableWidgetItem,
)
from data.DataStorage import DataStorage


class VentanaDatos(QWidget):
    """
    Ventana para mostrar los datos scrapeados.
    """
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.inicializarUI()

    def inicializarUI(self):
        """Inicializa la interfaz de usuario."""
        self.setWindowTitle("Datos Scrapeados")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.table = QTableWidget(self)
        self.table.setRowCount(len(self.data))
        self.table.setColumnCount(len(next(iter(self.data.values())).keys()))
        self.table.setHorizontalHeaderLabels(next(iter(self.data.values())).keys())
        layout.addWidget(self.table)

        for row, (key, value) in enumerate(self.data.items()):
            self.table.setVerticalHeaderItem(row, QTableWidgetItem(key))
            for col, (k, v) in enumerate(value.items()):
                self.table.setItem(row, col, QTableWidgetItem(str(v)))

        # Ajustar el tamaño de la columna de location
        location_index = list(next(iter(self.data.values())).keys()).index('location')
        self.table.setColumnWidth(location_index, 300)

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
                ds = DataStorage(self.data, "real_state_data.json", file)
                ds.save_data(self.data)
                QMessageBox.information(self, "Guardar Datos", f"Datos guardados en {file}")
            except Exception as e:
                QMessageBox.critical(self, "Error al Guardar Datos", f"Error al guardar los datos: {e}")
        else:
            QMessageBox.warning(self, "Guardar Datos", "Por favor, ingrese una ruta válida.")
