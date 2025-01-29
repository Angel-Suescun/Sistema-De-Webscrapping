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

## **Scraper y URLs:**

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
## **Excepciones:**

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
## **GUI**(Opcional):

```mermaid

classDiagram
    class UIManager {
        +show_main_window()
        +navigate_to(view: str)
    }

    class MainWindow {
        +init_UI()
        +show_results()
        +open_config()
    }

    class ResultsView {
        +display_results(data: List[Dict])
        +export_data(format: str)
    }

    class ConfigView {
        +set_scraper_settings(urls: List[str], filters: Dict)
    }

    class ReportView {
        +generate_report(format: str)
        +preview_report()
    }

    UIManager --> MainWindow
    MainWindow --> ResultsView
    MainWindow --> ConfigView
    MainWindow --> ReportView

```


## **Data**:

```mermaid
classDiagram
    class DataHandler {
        +process_data(data: List[Dict]) : List[Dict]
        +send_data(data: List[Dict], target: str)
        +save_data(data: List[Dict], format: str)
    }

    class DataStorage {
        +save_data(data: List[Dict], format: str)
        +load_data(file_path: str) : List[Dict]
    }

    class DataProcessor {
        +process_data(raw_data: List[Dict]) : List[Dict]
        +clean_data(data: List[Dict]) : List[Dict]
    }

    class DataCleaner {
        +delete_data(file_path: str)
    }

    class DataSender {
        +send_data(data: List[Dict], target: str)
    }

    DataHandler <|-- DataStorage
    DataHandler <|-- DataProcessor
    DataHandler <|-- DataSender

    DataProcessor --> DataSender 
    DataSender --> DataStorage 
    DataSender --> UIManager 
    DataSender --> ReportView  
    DataProcessor --> DataCleaner 


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

5. **Clases de la Interfaz Gráfica**:

   Se usara la libreria **PyQT6** para facilitar el trabajo

  - **`UIManager`**:
      - Controla la ventana principal y la navegación entre vistas.
      - Gestiona la navegación entre vistas y controla el flujo de interacción del usuario.

  - **`MainWindow`**:
      - Contiene los botones y menús principales de la interfaz.
     -  Recibe comandos de `UIManager` y gestiona la interacción con las vistas.

  - **`ResultsView`**:
      - Muestra los datos obtenidos en una tabla.
      - Recibe datos (generalmente de un scraper o base de datos) y los muestra en la interfaz de usuario.

  - **`ConfigView`**:
      - Permite configurar opciones del scraping (URLs, filtros, etc.).
      - Recibe entradas del usuario y las envía a un controlador de configuración.

  - **`ReportView`**:
      - Opción para exportar los datos en PDF o CSV.
      - Recibe los datos desde `ResultsView` y los exporta en el formato elegido por el usuario.
  
  6. **Clases Del Manejo de Datos**:

  - **`DataHandler`**:
      - Clase base abstracta para manejar la manipulación y distribución de los datos.
      - Define los métodos comunes `process_data()`, `send_data()` y `save_data()`.

  - **`DataStorage`**:
     - Se encarga de almacenar los datos procesados en archivos, como JSON o CSV.
     - Hereda de `DataHandler` y sobrescribe el método `save_data()` para guardar los datos en el formato especificado.
    - **Datos almacenados**:
       - Guarda los datos procesados o limpiados, listos para ser utilizados o exportados.

- **`DataProcessor`**:
     - Se encarga de procesar y limpiar los datos que recibe.
     - Hereda de `DataHandler` y sobrescribe los métodos `process_data()` y `clean_data()`
     - **Datos procesados**:
       - Convierte los datos crudos en un formato estandarizado, limpio y listo para su uso.


- **`DataSender`**:
     - Se encarga de enviar los datos procesados a otros módulos, como almacenamiento, interfaz gráfica o reporte.
     - Hereda de `DataHandler` y sobrescribe el método `send_data()`.
     - **Flujo de datos**:
       - Envía los datos procesados a los destinos correspondientes: `DataStorage` (para guardar), `UIManager` (para mostrar en la interfaz gráfica) o `ReportView` (para exportar los datos).

- **`DataCleaner`**:
     - Se encarga de eliminar los archivos o datos que ya no son necesarios una vez finalizada la ejecución del programa.



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


