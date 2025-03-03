class DataCleaner:
    """
    Clase para limpiar datos eliminando ciertas claves.
    """
    def __init__(self, data: dict) -> None:
        self.data = data
        self.clean_data()

    def clean_data(self) -> None:
        """
        Limpia los datos eliminando la clave 'url' de cada entrada.
        """
        for key in list(self.data.keys()):
            if isinstance(self.data[key], dict):
                self.data[key].pop("url", None)