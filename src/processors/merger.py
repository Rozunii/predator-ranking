"""
processors/merger.py
====================
Módulo para combinar los datasets de distintas fuentes
en un único DataFrame maestro.

Combina datos de PBDB (fósiles), PanTHERIA (mamíferos modernos)
y EltonTraits (aves modernas) en un solo dataset listo para
el cálculo de métricas y el ranking final.
"""

import pandas as pd

def merge_data(df_pbdb: pd.DataFrame, df_pantheria: pd.DataFrame, df_elton: pd.DataFrame) -> pd.DataFrame:
    """
    Combina los datasets de PBDB, PanTHERIA y EltonTraits en uno solo.

    Las columnas ausentes en cada fuente se rellenan automáticamente
    con NaN para su posterior imputación via RAG.

    Args:
        df_pbdb: DataFrame de especies fósiles desde PBDB.
        df_pantheria: DataFrame de mamíferos modernos desde PanTHERIA.
        df_elton: DataFrame de aves modernas desde EltonTraits.

    Returns:
        DataFrame maestro con todas las especies y columnas combinadas.
    """

    df_master = pd.concat([df_pbdb, df_pantheria, df_elton], ignore_index=True)
    print(f'\nMaster dataset: {len(df_master)} especies - {df_master.shape[1]} columnas')

    return df_master