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
from src.collectors import obtener_todos
from src.processors import imputar_entorno_dieta

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

if __name__ == '__main__':
    main()