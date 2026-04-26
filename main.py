"""
main.py
=======
Punto de entrada del pipeline de Predator Ranking.

Ejecuta la recolección, procesamiento y exportación de datos
de megadepredadores vertebrados a través de la historia geológica.

Uso:
    python main.py
"""

from src.collectors import obtener_todos

def main():
    """Ejecuta el pipeline completo de recolección de datos."""
    print('Predator ranking')

    df = obtener_todos()
    df.to_csv('data/raw/pbdb_raw.csv', index=False)

if __name__ == '__main__':
    main()