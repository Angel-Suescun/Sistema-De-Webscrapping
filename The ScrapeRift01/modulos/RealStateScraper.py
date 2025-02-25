import logging
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List, Dict
from modulos.BaseScraper import BaseScraper
import time

#? Clase del Realstate scraper
class RealStateScraper(BaseScraper):
    def __init__(self, base_url: str = 'https://www.ciencuadras.com/arriendo/bogota/apartamento', driver=None) -> None:
        super().__init__(base_url, driver)
    
    #* Metodo para extraer precios y guardarlos en listas
    def extract_price(self) -> List[str]:
        xpath_price = "//*[contains(@class, 'card__price-big') and not(ancestor::div[contains(@class, 'mat-tab-body-content')])]"
        # Espera hasta que al menos un elemento esté presente
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath_price))
        )
        elements = self.driver.find_elements(By.XPATH, xpath_price)
        prices = [el.text for el in elements if el.text]
        return prices[4:]   #! Se excluyen los 4 primeros precios pues estos se repiten en todas las paginas

    #* Metodo para extraer las ubicaciones y guardarlas en listas
    def extract_location(self) -> List[str]:
        xpath_location = "//*[contains(@class, 'card__location-label') and not(ancestor::div[contains(@class, 'mat-tab-body-content')])]"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath_location))
        )
        elements = self.driver.find_elements(By.XPATH, xpath_location)
        locations = [el.text for el in elements if el.text]
        return locations[4:]    #! Se excluyen las 4 primeros ubicaciones pues estos se repiten en todas las paginas

    #* Metodo para extraer los tamaños y guardarlos en listas
    def extract_size(self) -> List[str]:
        xpath_size = "//span[contains(text(), 'm2') and not(ancestor::div[contains(@class, 'mat-tab-body-content')])]"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath_size))
        )
        elements = self.driver.find_elements(By.XPATH, xpath_size)
        sizes = [el.text for el in elements if el.text]
        return sizes[4:]    #! Se excluyen los 4 primeros tamaños pues estos se repiten en todas las paginas
    
    #* Metodo para asignar cada precio, ubicacion y tamaño a una propiedad y guardarlo en un diccionario
    def combine_to_dict(self, prices: List[str], locations: List[str], sizes: List[str]) -> Dict:
        if not (len(prices) == len(locations) == len(sizes)):
            raise ValueError("Las listas de precios, ubicaciones y tamaños deben tener la misma longitud.")
        data = {}
        for i, (price, location, size) in enumerate(zip(prices, locations, sizes)):
            data[f"property_{i + 1}"] = {
                "price": price,
                "location": location,
                "size": size
            }
        return data

    #* Metodo para encontrar el boton para pasar de pagina
    def scroll_until_find_element(self, page: int, max_intentos: int = 3):
        intentos = 0
        self.driver.execute_script("document.body.style.zoom='30%'")
        while intentos < max_intentos:
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, f'[data-qa-id="cc-rs-rs_paginator_results_{page}"]'))
                )
                return element
            except Exception as e:
                logging.exception("Intento %s: No se encontró el botón de la página %s: %s", intentos+1, page, e)
                self.driver.execute_script("window.scrollBy(0, 300);")
                intentos += 1
        logging.error("Botón de la página %s no encontrado después de %s intentos.", page, max_intentos)
        return None

    #* Metodo para hallar la cantidad maxima de paginas que se pueden recorrer en el scraper
    def determine_max_page(self) -> int:
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME,"pagination"))
            )            
            pagination = self.driver.find_element(By.CLASS_NAME, "pagination")
            pages = pagination.find_elements(By.TAG_NAME, "li")
            max_page = 1
            for page in pages:
                try:
                    page_number = int(page.text)
                    if page_number > max_page:
                        max_page = page_number
                except ValueError:
                    continue
            logging.info("El número máximo de páginas es: %s", max_page)
        except Exception as e:
            logging.exception("Error al determinar el número máximo de páginas: %s", e)
            max_page = 1
        return max_page

    #* Metodo para guardar la información en un archivo de tipo .json
    def save_to_json(self, data: Dict, filename: str = 'real_state_data.json') -> None:
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            logging.info("Datos guardados en %s", filename)
        except Exception as e:
            logging.exception("Error al guardar el archivo JSON: %s", e)

    #* Metodo principal para scrapear la información
    def scrape(self) -> Dict:
        precios_totales = []
        ubicaciones_totales = []
        tamanos_totales = []
        max_pages = self.determine_max_page()
        pages_to_scrape = int(input('¿Cuántas páginas quieres scrapear? '))
        if pages_to_scrape > max_pages:
            raise ValueError("Número de páginas solicitado mayor al máximo disponible.")
        for i in range(1, pages_to_scrape + 1):
            if i != pages_to_scrape:
                boton = self.scroll_until_find_element(i + 1)
            prices = self.extract_price()
            locations = self.extract_location()
            sizes = self.extract_size()
            precios_totales.extend(prices)
            ubicaciones_totales.extend(locations)
            tamanos_totales.extend(sizes)
            if boton and i != pages_to_scrape:
                try:
                    ActionChains(self.driver).move_to_element(boton).click().perform()
                    # Se espera a que el botón sea visible nuevamente
                    WebDriverWait(self.driver, 10).until(lambda d: boton.is_displayed())
                except Exception as e:
                    logging.exception("Error al hacer clic en el botón de la página %s: %s", i, e)
        data = self.combine_to_dict(precios_totales, ubicaciones_totales, tamanos_totales)
        self.save_to_json(data)
        return data
