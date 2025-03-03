import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QLabel,
    QRadioButton, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem,
)
from PyQt6.QtCore import pyqtSignal
from modulos.UrlManager import RSUrl, WikiUrl
from modulos.RealStateScraper import RealStateScraper
from modulos.WikiScraper import LolScraper
from data.DataProcessor import DataProcessor
from data.DataStorage import DataStorage


class VentanaCiudad(QWidget):
    """
    Ventana para ingresar datos de scraping por ciudad.
    """
    enviar_datos_signal = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        """Inicializa la interfaz de usuario."""
        self.setWindowTitle("Scraping por Ciudad")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        label = QLabel("Ingrese la ciudad:")
        layout.addWidget(label)
        self.input_ciudad = QLineEdit(self)
        layout.addWidget(self.input_ciudad)

        label_paginas = QLabel("Ingrese el número de páginas a scrapear:")
        layout.addWidget(label_paginas)
        self.input_paginas = QLineEdit(self)
        layout.addWidget(self.input_paginas)

        self.btn_enviar = QPushButton("Enviar", self)
        self.btn_enviar.clicked.connect(self.enviar_datos)
        layout.addWidget(self.btn_enviar)

        self.setLayout(layout)

    def enviar_datos(self):
        """Emite la señal para enviar los datos de scraping."""
        ciudad = self.input_ciudad.text()
        paginas = int(self.input_paginas.text())
        self.enviar_datos_signal.emit(ciudad, paginas)
