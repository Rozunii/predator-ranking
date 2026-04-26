"""
collectors/pbdb.py
==================
Modulo para extraer datos de megadepredadores vertebrados
de la Paleobiology Database (PBDB) API.

API reference:
    https://paleobiodb.org/data1.2/taxa/list_doc.html
"""

import requests
import pandas as pd

grupos = [
    "Dinosauria",
    "Mosasauridae",
    "Plesiosauria", 
    "Chondrichthyes",    
    "Placodermi",       
    "Crocodylomorpha",  
    "Felidae",                
    "Cetacea",          
    "Boidae",           
    "Phorusrhacidae" 
]

def obtener_carnivoros(grupo: str) -> list[dict]:
    """
    Extrae todos los géneros de un grupo taxonómico desde la API de PBDB.

    Pagina automáticamente hasta agotar los registros disponibles.
    Solo incluye géneros con rango temporal documentado (fea y lla).

    Args:
        grupo: Nombre del taxón base a consultar (ej. "Dinosauria").
               Debe coincidir con la nomenclatura aceptada en PBDB.

    Returns:
        Lista de diccionarios, cada uno representando un género con
        las claves: Nombre, Grupo, Clase, Primera_aparicion,
        Ultima_aparicion, Dieta, Entorno.
    """
        
    my_list = []
    offset = 0

    while True:
        url = f'https://paleobiodb.org/data1.2/taxa/list.json?base_name={grupo}&rank=genus&show=ecospace,app,phylo&pres=regular&limit=500&offset={offset}'

        r = requests.get(url)
        r_json = r.json()

        for value in r_json['records']:
            if value.get('jdt') == 'carnivore' and value.get('fea') is not None and value.get('lla') is not None:      
                my_list.append({
                    'Nombre': value.get('nam'),
                    'Grupo': grupo,
                    'Clase': value.get('cll'),
                    'Primera_aparicion': value.get('fea'),
                    'Ultima_aparicion': value.get('lla'),
                    'Dieta': value.get('jdt'),
                    'Entorno': value.get('jev')
                })

        registros = r_json['records']
        if len(registros) < 500:
            break
        offset += 500
        print(f" {grupo} - Offset: {offset} - Carnívoros encontrados: {len(my_list)}")

    return my_list

def obtener_todos() -> pd.DataFrame:
    """
    Extrae y guarda megadepredadores de todos los grupos definidos en grupos.

    Itera sobre cada grupo taxonómico en grupos, consulta la API de PBDB
    y guarda los resultados en un único DataFrame.

    Returns:
        DataFrame con todos los géneros encontrados. Columnas:
        Nombre, Grupo, Clase, Primera_aparicion (Ma),
        Ultima_aparicion (Ma), Dieta, Entorno.
        Ma = millones de años antes del presente.
    """
    todos = []
    for grupo in grupos:
        print(f'Viendo: {grupo}')
        resultado = obtener_carnivoros(grupo)
        todos.extend(resultado)
        print(f'{len(resultado)} generos encontrados')
    
    df = pd.DataFrame(todos)
    return df

