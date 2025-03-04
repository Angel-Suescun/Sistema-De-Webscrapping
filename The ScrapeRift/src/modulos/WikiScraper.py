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
        self.champion = champion.capitalize()

    #* Extract the champion names from the League of Legends wiki
    def extract_champion_names(self):
        self.base_url = 'https://wiki.leagueoflegends.com/en-us/List_of_champions'
        self.initialize_webdriver()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-champion]'))
            )
            champion_elements = self.driver.find_elements(By.CSS_SELECTOR, '[data-champion]')
            champion_names = [element.get_attribute("data-champion") for element in champion_elements]
            sorted_champion_names = sorted(champion_names)
        except Exception as e:
            print(f"Error al extraer los nombres de los campeones: {e}")
            return []
        return sorted_champion_names
    
    #* Extract the health of the champion
    def extract_champion_health(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="Health_{self.champion}"]'))
            )
            health = self.driver.find_element(By.XPATH, f'//*[@id="Health_{self.champion}"]')
            return health.text if health else None
        except Exception as e:
            print(f"Error at extracting the health of the champion: {e}")
    
    #* Extract the mana of the champion    
    def extract_champion_mana(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="ResourceBar_{self.champion}"]'))
            )
            mana = self.driver.find_element(By.XPATH, f'//*[@id="ResourceBar_{self.champion}"]')
            return mana.text if mana else 'El campeon no usa mana'
        except Exception as e:
            print(f"Error at extracting the mana of the champion: {e}")
        
        
    
    #* Extract the health regen of the champion
    def extract_champion_health_regen(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="HealthRegen_{self.champion}"]'))
            )
            health_regen = self.driver.find_element(By.XPATH, f'//*[@id="HealthRegen_{self.champion}"]')
            return health_regen.text if health_regen else None
        except Exception as e:
            print(f"Error at extracting the health of the champion: {e}")
         
    
    #* Extract the mana regen of the champion
    def extract_champion_mana_regen(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="ResourceRegen_{self.champion}"]'))
            )
            mana_regen = self.driver.find_element(By.XPATH, f'//*[@id="ResourceRegen_{self.champion}"]')
            return mana_regen.text if mana_regen else "El campeon no usa mana"
        except Exception as e:
            print(f"Error at extracting the mana of the champion: {e}")
         

    #* Extract the armor of the champion
    def extract_champion_armor(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="Armor_{self.champion}"]'))
            )
            armor = self.driver.find_element(By.XPATH, f'//*[@id="Armor_{self.champion}"]')
            return armor.text if armor else None
        except Exception as e:
            print(f"Error at extracting the armor of the champion: {e}")
            
    
    #* Extract the attack damage of the champion
    def extract_champion_attack_damage(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="AttackDamage_{self.champion}"]'))
            )
            attack_damage = self.driver.find_element(By.XPATH, f'//*[@id="AttackDamage_{self.champion}"]')
            return attack_damage.text if attack_damage else None
        except Exception as e:
            print(f"Error at extracting the attack damage of the champion: {e}")
        
    
    #* Extract the magic resist of the champion
    def extract_champion_magic_resist(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="MagicResist_{self.champion}"]'))
            )
            magic_resist = self.driver.find_element(By.XPATH, f'//*[@id="MagicResist_{self.champion}"]')
            return magic_resist.text if magic_resist else None
        except Exception as e:
            print(f"Error at extracting the magic resist of the champion: {e}")
        
    
    #* Extract the crit damage of the champion
    def extract_champion_crit_damage(self):
        try:
            xpath_crit = '/html/body/div[4]/div[3]/div[5]/div[1]/div[5]/div[2]/div[8]/div[2]'
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath_crit))
            )
            crit_damage = self.driver.find_element(By.XPATH, xpath_crit)
            return crit_damage.text if crit_damage else None
        except Exception as e:
            print(f"Error at extracting the crit damage of the champion: {e}")
        
    
    #* Extract the move speed of the champion
    def excact_move_speed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID,f"MovementSpeed_{self.champion}"))
            )
            move_speed = self.driver.find_element(By.ID, f"MovementSpeed_{self.champion}")
            return move_speed.text if move_speed else None
        except Exception as e:
            print(f"Error at extracting the move speed of the champion: {e}")
        
    
    #* Extract the range of the champion
    def extract_champion_range(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID,f"AttackRange_{self.champion}"))
            )
            range = self.driver.find_element(By.ID, f"AttackRange_{self.champion}")
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
        time.sleep(1)
        health = self.extract_champion_health()
        mana = self.extract_champion_mana()
        health_regen = self.extract_champion_health_regen()
        mana_regen = self.extract_champion_mana_regen()
        armor = self.extract_champion_armor()
        attack_damage = self.extract_champion_attack_damage()
        magic_resist = self.extract_champion_magic_resist()
        crit_damage = self.extract_champion_crit_damage()
        move_speed = self.excact_move_speed()
        range = self.extract_champion_range()
        
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
    
            
            
