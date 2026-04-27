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
from src.processors import imputar_entorno_dieta, limpiar_pantheria, merge_data

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

if __name__ == '__main__':
    main()