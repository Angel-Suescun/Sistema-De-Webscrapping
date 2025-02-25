
#? Posible interfaz

def obtener_opcion_busqueda():
    opcion = input('¿Deseas buscar por ciudad o por barrio? (1: Ciudad, 2: Barrio): ')
    return opcion

def obtener_datos_ciudad():
    ciudad = input('Ingresa el nombre de la ciudad: ')
    return ciudad

def obtener_datos_barrio():
    ciudad = input('Ingresa el nombre de la ciudad: ')
    barrio = input('Ingresa el nombre del barrio: ')
    return ciudad, barrio

def obtener_nombre_campeon():
    return input('Ingresa el nombre del campeón: ')
