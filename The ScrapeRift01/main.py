from modulos.RealStateScraper import RealStateScraper
from modulos.WikiScraper import LolScraper
from modulos.UrlManager import RSUrl, WikiUrl
from modulos import ui

def main():
    #--- Para RealStateScrapper ---
    rs_url_manager = RSUrl()
    opcion = ui.obtener_opcion_busqueda()
    if opcion == '1':
        ciudad = ui.obtener_datos_ciudad()
        url = rs_url_manager.change_url(modo='1', ciudad=ciudad)
    elif opcion == '2':
        ciudad, barrio = ui.obtener_datos_barrio()
        url = rs_url_manager.change_url(modo='2', ciudad=ciudad, barrio=barrio)
    else:
        print("Opción inválida.")
        return
    with RealStateScraper(url) as scraper:
        realstate_data = scraper.scrape()
    
    # --- Para WikiScrapper ---
    wiki_url_manager = WikiUrl()
    nombre_campeon = ui.obtener_nombre_campeon()
    url_wiki = wiki_url_manager.change_url(champion=nombre_campeon)
    with LolScraper(base_url=url_wiki,champion=nombre_campeon) as wiki_scraper:
        champion_data = wiki_scraper.scrape()
        print(champion_data)

if __name__ == '__main__':
    main()
