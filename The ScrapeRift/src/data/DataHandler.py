import json
from abc import ABC, abstractmethod


class DataHandler(ABC):
    """
    Clase abstracta para manejar datos.
    """
    def __init__(self, data: dict, json_file: str):
        self.file = f"c:\\Users\\angel\\Desktop\\Angel\\Sistema-De-Webscrapping-main\\{json_file}"
        self.data = data

    @abstractmethod
    def process_data(self):
        """
        Método abstracto para procesar datos.
        """
        raise NotImplementedError

    @abstractmethod
    def send_data(self):
        """
        Método abstracto para enviar datos.
        """
        raise NotImplementedError

    @abstractmethod
    def save_data(self, data: dict):
        """
        Método abstracto para guardar datos.
        """
        raise NotImplementedError


class DataProcessor(DataHandler):
    """
    Clase para procesar datos desde un archivo JSON.
    """
    def __init__(self, json_file: str) -> None:
        super().__init__({}, json_file)
        self.data = self.process_data()

    def process_data(self) -> dict:
        """
        Procesa los datos desde el archivo JSON.

        Returns:
            dict: Datos procesados.
        """
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