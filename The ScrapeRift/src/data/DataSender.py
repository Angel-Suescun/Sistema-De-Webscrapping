import json
from .DataHandler import DataHandler

class DataSender(DataHandler):
    def __init__(self, data: dict, json_file: str) -> None:
        super().__init__(data, json_file)
        self.send_data()
    
    def send_data(self) -> None:
        print("Enviando datos...")
        return self.data
    
    def process_data(self) -> None:
        pass

    def save_data(self, data: dict) -> None:
        pass