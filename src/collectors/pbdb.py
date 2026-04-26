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
from src import config

def obtener_carnivoros(especie: str, grupo: str, clase: str) -> list[dict]:
    """
    Extrae los datos de una especie específica desde la API de PBDB.

    Args:
        especie: Nombre científico de la especie 
        grupo: Grupo taxonómico al que pertenece 
        clase: Clase taxonómica 

    Returns:
        Lista de diccionarios con las claves: Nombre, Grupo, Clase,
        Primera_aparicion, Ultima_aparicion, Dieta, Entorno.
    """
        
    my_list = []
    
    url = f'https://paleobiodb.org/data1.2/taxa/list.json?taxon_name={especie}&show=ecospace,app,phylo&pres=regular'
    r = requests.get(url)
    r_json = r.json()

    if 'records' not in r_json:
        print(f'No hay registros para: {especie}')
        return my_list
    
    for value in r_json['records']:
        if value.get('fea') is not None and value.get('lla') is not None:
            my_list.append({
                'Nombre': value.get('nam'),
                'Grupo': grupo,        
                'Clase': clase,        
                'Primera_aparicion': value.get('fea'),
                'Ultima_aparicion': value.get('lla'),
                'Dieta': value.get('jdt'),
                'Entorno': value.get('jev')
            })
    
    return my_list

def obtener_todos() -> pd.DataFrame:
    """
    Extrae y consolida datos de todas las especies definidas en ESPECIES_FOSILES.

    Itera sobre cada especie curada, consulta la API de PBDB
    y consolida los resultados en un único DataFrame.

    Returns:
        DataFrame con todas las especies encontradas. Columnas:
        Nombre, Grupo, Clase, Primera_aparicion (Ma),
        Ultima_aparicion (Ma), Dieta, Entorno.
        Ma = millones de años antes del presente.
    """
    
    todos = []
    for especie, grupo, clase in config.ESPECIES_FOSILES:
        print(f'Especie reconocida: {especie}')
        resultado = obtener_carnivoros(especie, grupo, clase)
        todos.extend(resultado)
        print(f'{len(resultado)} especies encontradas\n')
    
    df = pd.DataFrame(todos)
    return df

