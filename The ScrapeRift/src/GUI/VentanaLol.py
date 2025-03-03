import sys
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QMessageBox, QLabel,
    QLineEdit
)
from modulos.UrlManager import  WikiUrl
from modulos.WikiScraper import LolScraper
from data.DataProcessor import DataProcessor
from .VentanaDatosLol import VentanaDatosLoL


class VentanaLoL(QWidget):
    """
    Ventana para ingresar el nombre de un campeón de LoL y realizar el scraping.
    """
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.ventana_datos_lol = None  # Referencia a la ventana de datos

    def inicializarUI(self):
        """Inicializa la interfaz de usuario."""
        self.setWindowTitle("Scraping de LoL")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        label = QLabel("Ingrese el nombre del campeón:")
        layout.addWidget(label)

        self.input_campeon = QLineEdit(self)
        layout.addWidget(self.input_campeon)

        self.btn_enviar = QPushButton("Enviar", self)
        self.btn_enviar.clicked.connect(self.enviar_datos)
        layout.addWidget(self.btn_enviar)

        self.setLayout(layout)

    def enviar_datos(self):
        """Realiza el scraping del campeón de LoL y muestra los datos."""
        campeon = self.input_campeon.text()
        
        if campeon:
            # Realizar scraping
            url = WikiUrl().change_url(campeon)
            with LolScraper(base_url=url, champion=campeon) as scraper:
                scraper.scrape()
            dp = DataProcessor("champion_data.json")
            data = dp.process_data()
            self.ventana_datos_lol = VentanaDatosLoL(data)
            self.ventana_datos_lol.show()
            self.hide()

            if data:
                QMessageBox.information(self, "Scraping", f"Scraping completado para el campeón: {campeon}")
            else:
                QMessageBox.critical(self, "Error", "Error al realizar el scraping. Por favor, intente nuevamente.")
        else:
            QMessageBox.warning(self, "Scraping", "Por favor, ingrese un nombre de campeón válido.")

