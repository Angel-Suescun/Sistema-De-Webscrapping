import logging
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Optional

logging.basicConfig(level=logging.INFO)

#? Superclase para usar herencia y posible polimorfismo
class BaseScraper:
    def __init__(self, base_url: str, driver: Optional[WebDriver] = None) -> None:
        self.base_url = base_url
        if driver is None:
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver = driver

    def __enter__(self) -> "BaseScraper":
        try:
            self.driver.get(self.base_url)
            self.driver.maximize_window()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        except Exception as e:
            logging.exception("Error al inicializar el WebDriver: %s", e)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.driver:
            self.driver.quit()

    def wait_for_element(self, by: By, value: str, timeout: int = 10):
        #*Método auxiliar para esperar por un elemento usando esperas explícitas.
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except Exception as e:
            logging.exception("No se pudo encontrar el elemento (%s, %s): %s", by, value, e)
            return None
        
    def scrape(self):
        pass
