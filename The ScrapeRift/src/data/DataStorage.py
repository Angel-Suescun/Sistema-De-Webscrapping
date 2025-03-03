import json
from .DataHandler import DataHandler

class DataStorage(DataHandler):
    """
    Clase para guardar datos en un archivo JSON.
    """
    def __init__(self, data: dict, json_file: str, save_json: str) -> None:
        super().__init__(data, json_file)
        self.save_json = save_json
        self.save_data(data)

    def save_data(self, data: dict) -> None:
        """
        Guarda los datos en un archivo JSON.

        Args:
            data (dict): Datos a guardar.
        """
        try:
            with open(self.save_json, "w") as f:
                json.dump(data, f, indent=4)
            print(f"Datos guardados en {self.save_json}")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def process_data(self) -> None:
        pass

    def send_data(self) -> None:
        pass
