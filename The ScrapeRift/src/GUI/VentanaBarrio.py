from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel,QLineEdit
)
from PyQt6.QtCore import pyqtSignal

class VentanaBarrio(QWidget):
    """
    Ventana para ingresar datos de scraping por barrio.
    """
    enviar_datos_signal = pyqtSignal(str, str, int)

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        """Inicializa la interfaz de usuario."""
        self.setWindowTitle("Scraping por Barrio")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        label_ciudad = QLabel("Ingrese la ciudad:")
        layout.addWidget(label_ciudad)
        self.input_ciudad = QLineEdit(self)
        layout.addWidget(self.input_ciudad)

        label_barrio = QLabel("Ingrese el barrio:")
        layout.addWidget(label_barrio)
        self.input_barrio = QLineEdit(self)
        layout.addWidget(self.input_barrio)

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
        barrio = self.input_barrio.text()
        paginas = int(self.input_paginas.text())
        self.enviar_datos_signal.emit(ciudad, barrio, paginas)

