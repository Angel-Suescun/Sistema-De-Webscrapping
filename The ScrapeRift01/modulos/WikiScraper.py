from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modulos.BaseScraper import BaseScraper
import json
import time


#? Class to manage the LOL wiki scrapper
class LolScraper(BaseScraper):
    def __init__(self, base_url='https://wiki.leagueoflegends.com/en-us/', driver= None, champion = None):
        super().__init__(base_url, driver)
        self.champion = champion

    #* Extract the champion names from the League of Legends wiki
    def extract_champion_names(self):
        self.base_url = 'https://wiki.leagueoflegends.com/en-us/List_of_champions'
        self.initialize_webdriver()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-champion]'))
            )
            
            # Find the elements with the data-champion attribute
            champion_elements = self.driver.find_elements(By.CSS_SELECTOR, '[data-champion]')

            # Extract the data-champion attribute from each element
            champion_names = [element.get_attribute("data-champion") for element in champion_elements]
            sorted_champion_names = sorted(champion_names)
        except Exception as e:
            print(f"Error al extraer los nombres de los campeones: {e}")
            return []
        return sorted_champion_names
    
    #* Extract the health of the champion
    def extract_champion_health(self,champion):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="Health_{champion}"]'))
            )
            health = self.driver.find_element(By.XPATH, f'//*[@id="Health_{champion}"]')
            return health.text if health else None
        except Exception as e:
            print(f"Error at extracting the health of the champion: {e}")
    
    #* Extract the mana of the champion    
    def extract_champion_mana(self,champion):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="ResourceBar_{champion}"]'))
            )
            mana = self.driver.find_element(By.XPATH, f'//*[@id="ResourceBar_{champion}"]')
            return mana.text if mana else 'El campeon no usa mana'
        except Exception as e:
            print(f"Error at extracting the mana of the champion: {e}")
        
        
    
    #* Extract the health regen of the champion
    def extract_champion_health_regen(self, champion = None):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="HealthRegen_{champion}"]'))
            )
            health_regen = self.driver.find_element(By.XPATH, f'//*[@id="HealthRegen_{champion}"]')
            return health_regen.text if health_regen else None
        except Exception as e:
            print(f"Error at extracting the health of the champion: {e}")
         
    
    #* Extract the mana regen of the champion
    def extract_champion_mana_regen(self, champion = None):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="ResourceRegen_{champion}"]'))
            )
            mana_regen = self.driver.find_element(By.XPATH, f'//*[@id="ResourceRegen_{champion}"]')
            return mana_regen.text if mana_regen else "El campeon no usa mana"
        except Exception as e:
            print(f"Error at extracting the mana of the champion: {e}")
         

    #* Extract the armor of the champion
    def extract_champion_armor(self, champion = None):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="Armor_{champion}"]'))
            )
            armor = self.driver.find_element(By.XPATH, f'//*[@id="Armor_{champion}"]')
            return armor.text if armor else None
        except Exception as e:
            print(f"Error at extracting the armor of the champion: {e}")
            
    
    #* Extract the attack damage of the champion
    def extract_champion_attack_damage(self, champion = None):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="AttackDamage_{champion}"]'))
            )
            attack_damage = self.driver.find_element(By.XPATH, f'//*[@id="AttackDamage_{champion}"]')
            return attack_damage.text if attack_damage else None
        except Exception as e:
            print(f"Error at extracting the attack damage of the champion: {e}")
        
    
    #* Extract the magic resist of the champion
    def extract_champion_magic_resist(self, champion = None):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="MagicResist_{champion}"]'))
            )
            magic_resist = self.driver.find_element(By.XPATH, f'//*[@id="MagicResist_{champion}"]')
            return magic_resist.text if magic_resist else None
        except Exception as e:
            print(f"Error at extracting the magic resist of the champion: {e}")
        
    
    #* Extract the crit damage of the champion
    def extract_champion_crit_damage(self, champion=None):
        try:
            # Usa el XPath correcto según lo que inspecciones en el navegador.
            xpath_crit = '/html/body/div[4]/div[3]/div[5]/div[1]/div[5]/div[2]/div[8]/div[2]'
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath_crit))
            )
            crit_damage = self.driver.find_element(By.XPATH, xpath_crit)
            return crit_damage.text if crit_damage else None
        except Exception as e:
            print(f"Error at extracting the crit damage of the champion: {e}")
        
    
    #* Extract the move speed of the champion
    def excact_move_speed(self, champion = None):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID,f"MovementSpeed_{champion}"))
            )
            move_speed = self.driver.find_element(By.ID, f"MovementSpeed_{champion}")
            return move_speed.text if move_speed else None
        except Exception as e:
            print(f"Error at extracting the move speed of the champion: {e}")
        
    
    #* Extract the range of the champion
    def extract_champion_range(self, champion = None):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID,f"AttackRange_{champion}"))
            )
            range = self.driver.find_element(By.ID, f"AttackRange_{champion}")
            return range.text if range else None
        except Exception as e:
            print(f"Error at extracting the range of the champion: {e}")
        
    
    #* Save the data to a JSON file
    def save_to_json(self, data, filename='champion_data.json'):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print(f"Datos guardados en {filename}")
        except Exception as e:
            print(f"Error al guardar el archivo JSON: {e}")
    
    #* Scrape all the information of the champion
    def scrape(self):
        time.sleep(2)
        health = self.extract_champion_health(self.champion)
        mana = self.extract_champion_mana(self.champion)
        health_regen = self.extract_champion_health_regen(self.champion)
        mana_regen = self.extract_champion_mana_regen(self.champion)
        armor = self.extract_champion_armor(self.champion)
        attack_damage = self.extract_champion_attack_damage(self.champion)
        magic_resist = self.extract_champion_magic_resist(self.champion)
        crit_damage = self.extract_champion_crit_damage(self.champion)
        move_speed = self.excact_move_speed(self.champion)
        range = self.extract_champion_range(self.champion)
        
        dictionary = {
            'Champion': self.champion,
            'Health': health,
            'Mana': mana,
            'Health Regen': health_regen,
            'Mana Regen': mana_regen,
            'Armor': armor,
            'Attack Damage': attack_damage,
            'Magic Resist': magic_resist,
            'Crit Damage': crit_damage,
            'Move Speed': move_speed,
            'Range': range
        }
        
        self.save_to_json(dictionary)
        
        return dictionary
    
            
            