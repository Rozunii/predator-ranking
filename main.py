"""
main.py
=======
Punto de entrada del pipeline de Predator Ranking.

Ejecuta la recolección, procesamiento y exportación de datos
de megadepredadores vertebrados a través de la historia geológica.

Uso:
    python main.py
"""

import os
import pandas as pd
from src.collectors import obtener_todos, obtener_modernos, obtener_modernos_aves
from src.processors import imputar_entorno_dieta, limpiar_pantheria, merge_data, enriquecer_modernos, imputar_dieta_modernos
from src.rag import obtener_textos, inicializar_db, indexar_textos, extraer_masa_corporal
from src.processors.manual_masses import MASAS_MANUALES

def main():
    """Ejecuta el pipeline completo de recolección de datos."""
    print('Predator ranking')

    if os.path.exists('data/raw/pbdb_raw.csv'):
        df = pd.read_csv('data/raw/pbdb_raw.csv')
    else: 
        df = obtener_todos()
        df.to_csv('data/raw/pbdb_raw.csv', index=False)

    df = imputar_entorno_dieta(df)

    df.to_csv('data/processed/pbdb_clean.csv', index=False)

    df_pantheria = obtener_modernos('data/raw/PanTHERIA_1-0_WR93_Aug2008.txt')

    df_pantheria.to_csv('data/raw/pantheria_raw.csv', index=False)
    df_pantheria = limpiar_pantheria(df_pantheria)

    df_pantheria.to_csv('data/processed/pantheria_clean.csv', index=False)

    df_elton = obtener_modernos_aves('data/raw/BirdFuncDat.txt')

    df_elton.to_csv('data/raw/elton_raw.csv', index=False)
    df_elton.to_csv('data/processed/elton_clean.csv', index=False)

    df_master = merge_data(df, df_pantheria, df_elton)
    df_master.to_csv('data/processed/master_raw.csv', index=False)

    df_master = enriquecer_modernos(df_master)
    df_master = imputar_dieta_modernos(df_master)

    df_master.to_csv('data/processed/master_clean.csv', index=False)

    # RAG desactivado temporalmente - PubMed no tiene cobertura suficiente
    # de literatura paleontológica. Se reactivará con fuente alternativa.
    # chroma = inicializar_db()
    # sin_masa = df_master[df_master['Masa_g'].isnull()]['Nombre'].to_list()
    # for especie in sin_masa:
    #     textos = obtener_textos(especie)
    #     indexar_textos(chroma, especie, textos)
    #     masa = extraer_masa_corporal(chroma, especie)
    #     if masa != 'NO_ENCONTRADO':
    #         try:
    #             df_master.loc[df_master['Nombre'] == especie, 'Masa_g'] = float(masa.split()[0])
    #         except:
    #             print(f'  [{especie}] No se pudo convertir: {masa}')

    # Masas curadas manualmente con fuentes científicas citadas
    for especie, datos in MASAS_MANUALES.items():
        mask = (df_master['Nombre'] == especie) & (df_master['Masa_g'].isnull())
        if mask.any():
            df_master.loc[mask, 'Masa_g'] = datos['masa_kg'] * 1000

    df_master.to_csv('data/processed/master_clean.csv', index=False)
    print(f'\nMaster dataset actualizado: {df_master["Masa_g"].isnull().sum()} especies sin masa corporal')


if __name__ == '__main__':
    main()