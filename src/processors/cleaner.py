"""
processors/cleaner.py
==================
Modulo para limpiar los raw datasets.
"""

import pandas as pd
from src import config


def imputar_entorno_dieta(df: pd.DataFrame) -> pd.DataFrame:
    """
    Imputa el entorno respecto a la clase a los datos nulos en la columna Entorno.

    Cuando un Entorno es nulo, se le imputa el entorno
    respecto a la clase que tenga mas afinidad.

    Args:
        df: DataFrame crudo con posibles nulos en Entorno

    Returns:
        DataFrame sin nulos en columna Entorno.
    """
    nulos = df.isna().sum()
    df['Entorno'] = df['Entorno'].fillna(df['Clase'].map(config.ENTORNO_POR_CLASE))
    for especie, entorno in config.ENTORNO_EXCEPCIONES.items():
        df.loc[df['Nombre'] == especie, 'Entorno'] = entorno
    df['Dieta'] = df['Dieta'].fillna('carnivore')
    print(f'Nulos antes:\n{nulos}\n \nNulos despues:\n{df.isna().sum()}\n')
    return df


def limpiar_pantheria(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el dataset crudo de PanTHERIA reemplazando valores faltantes.

    PanTHERIA codifica datos ausentes como -999. Esta función los
    convierte a NaN para un manejo correcto en el pipeline.

    Args:
        df: DataFrame crudo de PanTHERIA con valores -999.

    Returns:
        DataFrame con valores -999 reemplazados por NaN.
    """
    
    df = df.replace(-999, None)

    return df

