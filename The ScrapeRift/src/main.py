# Version: 1.0

import sys
from PyQt6.QtWidgets import QApplication
from GUI.VentanaPrincipal import VentanaPrincipal

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())
