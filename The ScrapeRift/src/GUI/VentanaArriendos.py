from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QLabel,
    QRadioButton
)
from PyQt6.QtCore import pyqtSignal

class VentanaArriendos(QWidget):
    """
    Ventana para seleccionar opciones de scraping de arriendos.
    """
    seleccionar_opcion_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        """Inicializa la interfaz de usuario."""
        self.setWindowTitle("Opciones de Scraping de Arriendos")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        
        label = QLabel("Seleccione una opción:")
        layout.addWidget(label)

        self.radio_ciudad = QRadioButton("Por ciudad")
        self.radio_barrio = QRadioButton("Por barrio")
        layout.addWidget(self.radio_ciudad)
        layout.addWidget(self.radio_barrio)

        self.btn_siguiente = QPushButton("Siguiente", self)
        self.btn_siguiente.clicked.connect(self.siguiente)
        layout.addWidget(self.btn_siguiente)

        self.setLayout(layout)

    def siguiente(self):
        """Emite la señal para seleccionar la opción de scraping."""
        if self.radio_ciudad.isChecked():
            self.seleccionar_opcion_signal.emit("ciudad")
        elif self.radio_barrio.isChecked():
            self.seleccionar_opcion_signal.emit("barrio")

