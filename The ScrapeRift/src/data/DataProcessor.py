import json
from .DataHandler import DataHandler

class DataProcessor(DataHandler):
    def __init__(self, json_file: str) -> None:
        super().__init__({}, json_file)
        self.file = json_file
        self.data = self.process_data()

    def process_data(self) -> dict:
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError("Formato de archivo no válido. Debe ser un diccionario JSON.")
            return data
        except FileNotFoundError:
            print(f"Archivo no encontrado: {self.file}")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON: {self.file}")
        except ValueError as ve:
            print(f"Error de valor: {ve}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        print("Error al cargar el archivo. Creando un diccionario vacío.")
        return {}

    def save_data(self, data: dict) -> None:
        pass

    def send_data(self) -> None:
        pass
    
