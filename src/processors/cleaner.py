"""
processors/cleaner.py
==================
Modulo para limpiar duplicados e imputar datos nulos en pbdb_raw.csv.
"""

import pandas as pd

ENTORNO_POR_CLASE = {
    'Reptilia': 'terrestrial',
    'Aves': 'terrestrial',
    'Chondrichthyes': 'marine',
    'Mammalia': 'terrestrial',
    'Placodermi': 'marine',
    'Saurischia': 'terrestrial'
}

def eliminar_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina géneros duplicados conservando el registro más antiguo.

    Cuando un género aparece en más de un grupo taxonómico,
    se conserva la ocurrencia con mayor Primera_aparicion,
    ya que representa el registro fósil más completo.

    Args:
        df: DataFrame crudo con posibles duplicados en Nombre.

    Returns:
        DataFrame sin duplicados en columna Nombre.
    """ 

    df['Duracion_Ma'] = df['Primera_aparicion'] - df['Ultima_aparicion']

    antes = len(df)

    df = df.sort_values('Duracion_Ma', ascending=False)
    df = df.drop_duplicates(subset='Nombre', keep='first')

    print(f'Dimensiones del dataset antes: {antes} - Dimensiones del dataset despues: {len(df)}\n')

    return df


def imputar_entorno(df: pd.DataFrame) -> pd.DataFrame:
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
    df['Entorno'] = df['Entorno'].fillna(df['Clase'].map(ENTORNO_POR_CLASE))
    print(f'Nulos antes:\n{nulos}\n \nNulos despues:\n{df.isna().sum()}\n')
    return df
