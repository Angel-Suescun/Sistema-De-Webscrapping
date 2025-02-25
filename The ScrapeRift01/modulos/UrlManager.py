
#* Clase padre de los urls
class Url:
    def __init__(self, url):
        self.url = url

    def change_url(self, **kwargs):
        raise NotImplementedError("Subclasses must implement this method.")


#* Subclase de Url para manejar los url de realstate (Ciencuadras)
class RSUrl(Url):
    def __init__(self, base_url="https://www.ciencuadras.com/arriendo"):
        super().__init__(base_url)
    
    #* Metodo para cambiar de url si es requerido
    def change_url(self, modo, ciudad, barrio=None):
        if modo == '1':
            # Busqueda por ciudad
            self.url = f"{self.url}/{ciudad}"
        elif modo == '2' and barrio:
            self.url = f"{self.url}/{ciudad}/{barrio}/apartamento"
        else:
            raise ValueError("Parámetros insuficientes para cambiar la URL.")
        return self.url


#* Subclase de url para manejar los url de la wiki de LoL
class WikiUrl(Url):
    def __init__(self, base_url="https://wiki.leagueoflegends.com/en-us/"):
        super().__init__(base_url)
        self.champion = None
    #* Metodo para cambiar de url si es requerido
    def change_url(self, champion):
        self.url = f"{self.url}{champion}"
        self.champion = champion
        return self.url
