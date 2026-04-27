"""
processors/enricher.py
======================
Módulo para enriquecer el dataset maestro con información
proveniente de la lista curada de especies en config.py.

Agrega Grupo, Clase, Entorno y rango temporal a las especies
modernas, e imputa la columna Dieta desde el nivel trófico
de PanTHERIA.
"""

import pandas as pd 
from src import config

def enriquecer_modernos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Enriquece el dataset maestro con Grupo, Clase y Entorno desde config.py.

    Las especies modernas llegan sin Grupo ni Clase porque provienen
    de PanTHERIA y EltonTraits. Esta función cruza por nombre con
    ESPECIES_MODERNAS para rellenar esos valores faltantes.

    Args:
        df: DataFrame maestro combinado con posibles nulos en Grupo y Clase.

    Returns:
        DataFrame con Grupo y Clase completos para todas las especies.
    """
    df_config = pd.DataFrame(config.ESPECIES_MODERNAS, columns=['Nombre', 'Grupo_new', 'Clase_new', 'Entorno_new'])

    df = df.merge(df_config, on='Nombre', how='left')
    df['Grupo'] = df['Grupo'].fillna(df['Grupo_new'])
    df['Clase'] = df['Clase'].fillna(df['Clase_new'])
    df['Entorno'] = df['Entorno'].fillna(df['Entorno_new'])
    df = df.drop(columns=['Grupo_new', 'Clase_new', 'Entorno_new'])
    return df

def imputar_dieta_modernos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Imputa la columna Dieta para especies modernas desde Nivel_trofico.

    PanTHERIA codifica la dieta como un nivel trófico numérico (1-3).
    Esta función lo convierte a texto consistente con el resto del dataset
    y elimina la columna Nivel_trofico una vez procesada.

    Args:
        df: DataFrame maestro con columna Nivel_trofico de PanTHERIA.

    Returns:
        DataFrame con Dieta imputada y columna Nivel_trofico eliminada.
    """
    dietas = {
        1: 'herviboro',
        2: 'omnivoro',
        3: 'carnivoro'
    }

    df['Dieta'] = df['Dieta'].fillna(df['Nivel_trofico'].map(dietas))
    df = df.drop(columns=['Nivel_trofico'])
    df['Dieta'] = df['Dieta'].replace('VertFishScav', 'carnivore')

    return df