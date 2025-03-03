from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QMessageBox)
from PyQt6.QtCore import pyqtSignal
from modulos.UrlManager import RSUrl
from modulos.RealStateScraper import RealStateScraper
from data.DataProcessor import DataProcessor
from .VentanaArriendos import VentanaArriendos
from .VentanaCiudad import VentanaCiudad
from .VentanaBarrio import VentanaBarrio
from .VentanaDatos import VentanaDatos
from .VentanaLol import VentanaLoL

class VentanaPrincipal(QWidget):
    """
    Ventana principal que permite seleccionar entre scraping de arriendos
    o scraping de LoL.
    """
    cambiar_interfaz_signal = pyqtSignal()

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.inicializarUI()
        
        # Mantener referencias de las ventanas secundarias
        self.ventana_arriendos = VentanaArriendos()
        self.ventana_ciudad = VentanaCiudad()
        self.ventana_barrio = VentanaBarrio()
        self.ventana_datos = None  # Referencia a la ventana de datos
        self.ventana_lol = VentanaLoL()

        self.cambiar_interfaz_signal.connect(self.ventana_arriendos.show)
        self.cambiar_interfaz_signal.connect(self.hide)

        self.ventana_arriendos.seleccionar_opcion_signal.connect(
            lambda opcion: self.ventana_ciudad.show() if opcion == "ciudad"
            else self.ventana_barrio.show()
        )
        self.ventana_arriendos.seleccionar_opcion_signal.connect(
            self.ventana_arriendos.hide
        )

        self.ventana_ciudad.enviar_datos_signal.connect(
            lambda ciudad, paginas: (
                self.manejar_scraping_ciudad(ciudad, paginas),
                self.ventana_ciudad.hide()
            )
        )
        self.ventana_barrio.enviar_datos_signal.connect(
            lambda ciudad, barrio, paginas: (
                self.manejar_scraping_barrio(ciudad, barrio, paginas),
                self.ventana_barrio.hide()
            )
        )

    def inicializarUI(self):
        """Inicializa la interfaz de usuario."""
        self.setWindowTitle("Scraping Options")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.btn_arriendos = QPushButton("Scrapear página de arriendos", self)
        self.btn_arriendos.clicked.connect(self.scrapear_arriendos)
        layout.addWidget(self.btn_arriendos)

        self.btn_lol = QPushButton("Scrapear página de LoL", self)
        self.btn_lol.clicked.connect(self.scrapear_lol)
        layout.addWidget(self.btn_lol)

        self.setLayout(layout)
        self.show()

    def scrapear_arriendos(self):
        """Cambia a la interfaz de scraping de arriendos."""
        self.cambiar_interfaz_signal.emit()

    def scrapear_lol(self):
        """Cambia a la interfaz de scraping de LoL."""
        self.ventana_lol.show()
        self.hide()

    def manejar_scraping_ciudad(self, ciudad, paginas):
        """
        Maneja el scraping de arriendos por ciudad.

        Args:
            ciudad (str): Nombre de la ciudad.
            paginas (int): Número de páginas a scrapear.
        """
        print(f"Iniciando scraping de página de arriendos por ciudad: "
                f"{ciudad} con {paginas} páginas")
        rs_url_manager = RSUrl()
        url = rs_url_manager.change_url(modo='1', ciudad=ciudad)
        with RealStateScraper(paginas, url) as scraper:
            scraper.scrape()
        dp = DataProcessor("real_state_data.json")
        data = dp.process_data()
        self.ventana_datos = VentanaDatos(data)
        self.ventana_datos.show()

        QMessageBox.information(self, "Scraping", 
                                f"Scraping completado para la ciudad: {ciudad}")

    def manejar_scraping_barrio(self, ciudad, barrio, paginas):
        """
        Maneja el scraping de arriendos por barrio.

        Args:
            ciudad (str): Nombre de la ciudad.
            barrio (str): Nombre del barrio.
            paginas (int): Número de páginas a scrapear.
        """
        print(f"Iniciando scraping de página de arriendos por ciudad: "
                f"{ciudad} y barrio: {barrio} con {paginas} páginas")
        rs_url_manager = RSUrl()
        url = rs_url_manager.change_url(modo='2', ciudad=ciudad, barrio=barrio)
        with RealStateScraper(paginas, url) as scraper:
            scraper.scrape()
        dp = DataProcessor("real_state_data.json")
        data = dp.process_data()
        self.ventana_datos = VentanaDatos(data)
        self.ventana_datos.show()

        QMessageBox.information(self, "Scraping", 
                                f"Scraping completado para el barrio: {barrio}")

