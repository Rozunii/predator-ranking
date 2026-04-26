"""
collectors/eltontraits.py
=======================
Módulo para extraer datos de aves depredadoras modernas
desde el dataset estático EltonTraits 1.0 (Wilman et al., 2014).

Dataset Reference:
    Wilman et al. (2014). EltonTraits 1.0: Species-level foraging attributes
    of the world's birds and mammals.
    Ecology 95(7): 2027. https://doi.org/10.1890/13-1917.
"""

import pandas as pd
from src import config


def obtener_modernos_aves(filepath: str) -> pd.DataFrame:
    """
    Extrae datos de aves depredadoras modernas desde EltonTraits.

    Lee el archivo BirdFuncDat y filtra las especies definidas
    en ESPECIES_MODERNAS, retornando masa corporal y dieta.

    Args:
        filepath: Ruta al archivo BirdFuncDat.txt de EltonTraits.

    Returns:
        DataFrame con las especies encontradas. Columnas:
        Nombre, Masa_g, Dieta, %_Vertebrados_Dieta.
    """

    df_modernos_aves = pd.read_csv(filepath, sep='\t', encoding='latin1')
    df_modernos_aves = df_modernos_aves[['Scientific', 'BodyMass-Value', 'Diet-5Cat', 'Diet-Vend']]

    df_modernos_aves = df_modernos_aves.rename(columns={
    'Scientific': 'Nombre',
    'BodyMass-Value': 'Masa_g',
    'Diet-5Cat': 'Dieta',
    'Diet-Vend': '%_Vertebrados_Dieta'
    })

    nombres = [especie[0] for especie in config.ESPECIES_MODERNAS]

    df_modernos_aves = df_modernos_aves[df_modernos_aves['Nombre'].isin(nombres)]

    print(f'\nEspecies modernas encontradas en Eltontraits: {len(df_modernos_aves)}')
    print("\n",df_modernos_aves[['Nombre', 'Masa_g', 'Dieta']].to_string())

    return df_modernos_aves