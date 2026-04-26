"""
collectors/pantheria.py
=======================
Módulo para extraer datos de megadepredadores modernos
desde el dataset estático PanTHERIA v1.0 (Wilson & Reeder, 2005).

Dataset Reference:
    Jones et al. (2009). PanTHERIA: a species-level database of life history,
    ecology, and geography of extant and recently extinct mammals.
    Ecology 90(9): 2648. https://doi.org/10.1890/08-1494.1
"""

import pandas as pd
from src import config


def obtener_modernos(filepath: str) -> pd.DataFrame:
    """
    Extrae y consolida datos de todas las especies definidas en ESPECIES_MODERNAS.

    Consulta el dataset de PanTHERIA y filtra columnas para
    consolidar los resultados en un único DataFrame.

    Returns:
        DataFrame con todas las especies encontradas. Columnas:
        Nombre, Grupo, Clase, Masa corporal, Rango geografico, Tasa metabolica basal, Dieta.
    """

    df_modernos = pd.read_csv(filepath, sep='\t')
    df_modernos = df_modernos[['MSW93_Genus', 'MSW93_Binomial', '5-1_AdultBodyMass_g', '6-2_TrophicLevel', '26-1_GR_Area_km2', '18-1_BasalMetRate_mLO2hr']]

    df_modernos = df_modernos.rename(columns={
    'MSW93_Binomial': 'Nombre',
    '5-1_AdultBodyMass_g': 'Masa_g',
    '6-2_TrophicLevel': 'Nivel_trofico',
    '26-1_GR_Area_km2': 'Rango_geografico_km2',
    '18-1_BasalMetRate_mLO2hr': 'Tasa_metabolica',
    'MSW93_Genus': 'Genero'
    })

    nombres = [especie[0] for especie in config.ESPECIES_MODERNAS]

    df_modernos = df_modernos[df_modernos['Nombre'].isin(nombres)]

    print(f'Especies modernas encontradas en PanTHERIA: {len(df_modernos)}\n')
    print("\n",df_modernos[['Nombre', 'Masa_g', 'Nivel_trofico']].to_string())

    return df_modernos


