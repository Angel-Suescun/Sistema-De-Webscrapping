# Sistema-De-Webscrapping

# Definición de alternativa

## Contexto y Motivación

El **web scraping** es una técnica que permite automatizar la extracción de datos de sitios web, facilitando el acceso y análisis de información de manera eficiente.
Entre sus principales ventajas están:

- **Automatización**: Reduce el tiempo y esfuerzo de la recopilación manual.
- **Eficiencia**: Procesa grandes volúmenes de datos rápidamente.
- **Acceso en tiempo real**: Garantiza información actualizada.
- **Flexibilidad**: Aplicable a diversos tipos de sitios web y datos.
- **Estructuración de datos**: Convierte datos no organizados en formatos como CSV o JSON.

Este proyecto se eligió porque, entre las alternativas disponibles, tiene un objetivo final claro: crear una herramienta práctica que permita analizar datos de sitios dinámicos, como plataformas de comercio. Además, la implementación con principios de **Programación Orientada a Objetos** garantiza un diseño modular y adaptable.

<ins>Mas informacion en:</ins> [Web scraping: qué es, funcionamiento y ventajas](https://www.esic.edu/rethink/tecnologia/web-scraping-que-es-funcionamiento-ventajas-c) 

##  Objetivos:

- ## Objetivo General
  - Desarrollar una aplicación que emule un sistema de **web scraping** utilizando **Python** y los principios de **Programación Orientada a Objetos (POO)** enseñados en clase, con el fin de extraer, organizar y analizar datos de sitios web dinámicos.

 - ## Objetivos Específicos
    1. Desarrollar un sistema de scraping que permita extraer texto de sitios web tipo **wiki**, identificando y organizando la información relevante.
    2. Implementar un proceso de extracción de publicaciones de plataformas de bienes raíces, generar reportes con los datos recolectados y organizarlos por ciudad o localidad.
    3. Aplicar principios de **POO** para estructurar el código en clases y objetos que faciliten la reutilización, extensión y mantenimiento del sistema.


## Justificacion

Este proyecto se eligió por su enfoque práctico y aplicable en el mundo real. El **web scraping** permite automatizar la recolección de datos de sitios dinámicos, lo cual es útil en áreas como el análisis de mercado o bienes raíces. Además, aplicar **Programación Orientada a Objetos (POO)** garantiza un código modular, escalable y fácil de mantener, lo que favorece su reutilización y expansión futura.

Este proyecto no solo aborda un problema concreto de recolección y organización de datos, sino que también brinda experiencia valiosa en herramientas de programación avanzadas y en la creación de soluciones eficientes y adaptables.

# Diagrama De Clases

```mermaid
classDiagram
    class ScraperUrl {
        - url: String
        + validate_url(): bool
        + get_url(): String
    }

    class LOLUrl {
        - url: ScraperUrl
        + validate_url(): bool
        + is_champion_url(): bool
        + is_type_url(): bool
    }

    class RSUrl {
        - url: ScraperUrl
        + validate_url(): bool
        + is_location_url(): bool
        + is_size_url(): bool
    }

    class BaseScraper {
        - url: ScraperUrl
        - headers: Dict
        + get_html(timeout: int = 10): String
    }

    class LOLScraper {
        - url: LOLUrl
        - soup: BeautifulSoup
        + parse_champions(): List[Dict]
    }

    class RSScraper {
        - url: RSUrl
        - soup: BeautifulSoup
        + parse_info(): List[Dict]
    }

    %% Definir herencias después
    
    BaseScraper <|-- RSScraper
    

    %% Definir relaciones de composición primero
    ScraperUrl <|-- LOLUrl
    ScraperUrl <|-- RSUrl

    LOLUrl *-- LOLScraper
    RSUrl *-- RSScraper
    ScraperUrl *-- BaseScraper
    BaseScraper <|-- LOLScraper


```
```mermaid

classDiagram
    class ScraperException {
        +message: String
    }

    class ConnectionError {
        +message: String
    }


    class InvalidURLError {
        +message: String
    }

    class HTTPError {
        +message: String
        +status_code: int
    }

    ScraperException <|-- ConnectionError
    ScraperException <|-- InvalidURLError
    ScraperException <|-- HTTPError
```

## **Solución Preliminar**

### **Clases y Componentes**

1. **`ScraperUrl`**:
   - Se encarga de manejar y validar URLs.

2. **`BaseScraper`**:
   - Clase genérica que realiza solicitudes HTTP y devuelve el contenido HTML.
   - Utiliza composición con `ScraperUrl`.

3. **Clases especializadas**:
   - **`LOLScraper`**:
     - Diseñada para extraer estadísticas de campeones desde la wiki de League of Legends.
     - Utiliza herencia del `BaseScraper` y se compone de un `LOLUrl`

   - **`RSScraper`**:
     - Diseñada para extraer información de propiedades desde sitios de bienes raíces.
     - Utiliza herencia del `BaseScraper` y se compone de un `RSUrl`
     - Datos que extraerá:
       - **Precio**: Muestra el precio de cada propiedad.
       - **Tamaño**: Área en metros cuadrados.
       - **Ciudad**: Ubicación de la propiedad.

4. **Excepciones Personalizadas**:
   - Definen errores específicos como `ConnectionError`, `InvalidURLError` y `HTTPError`.

### **Estructura de Archivos**
```
The_ScrapeRift/
│── src/
│   ├── GUI/
│   │   ├── __init__.py
│   ├── configuration/
│   │   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   ├── errorManagement/
│   │   ├── __init__.py
│   ├── executionControl/
│   │   ├── __init__.py
│   ├── moduleController/
│   │   ├── __init__.py
│   ├── scrapper/
│   │   ├── __init__.py
│   ├── url/
│   │   ├── __init__.py
│   ├── __init__.py
│   ├── main.py
│── README.md
```


