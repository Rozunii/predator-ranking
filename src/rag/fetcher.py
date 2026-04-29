"""
rag/fetcher.py
==============
Módulo para descargar papers científicos desde PubMed Central
usando la API Entrez de NCBI.

Para cada especie busca papers relacionados con masa corporal,
rango temporal y distribución geográfica.

API Reference:
    https://www.ncbi.nlm.nih.gov/books/NBK25497/
"""

from Bio import Entrez
import time

def buscar_papers(especie: str) -> list:
    """
    Busca papers en PubMed relacionados con la masa corporal de una especie.

    Args:
        especie: Nombre científico de la especie (ej. "Tyrannosaurus rex").

    Returns:
        Lista de IDs de papers encontrados en PubMed.
    """

    Entrez.email = 'sebastian.espinosa251@gmail.com'

    handle = Entrez.esearch(db='pubmed', term=f'{especie} body mass', retmax=5)
    record = Entrez.read(handle)
    handle.close()

    return record['IdList']

def descargar_paper(paper_id: str) -> str:
    """
    Descarga el abstract de un paper de PubMed dado su ID.

    Args:
        paper_id: ID numérico del paper en PubMed.

    Returns:
        Texto del abstract como string.
    """
    handle = Entrez.efetch(db='pubmed', id=paper_id, rettype='abstract', retmode='text')
    texto = handle.read()
    handle.close()

    return texto

def obtener_textos(especie: str) -> list[str]:
    """
    Busca y descarga los abstracts de papers sobre una especie desde PubMed.

    Args:
        especie: Nombre científico de la especie (ej. "Tyrannosaurus rex").

    Returns:
        Lista de strings, cada uno con el texto de un abstract.
    """

    ids= buscar_papers(especie)
    textos = []

    for paper_id in ids:
        texto = descargar_paper(paper_id)
        textos.append(texto)
        time.sleep(0.4)

    print(f'{especie}: {len(textos)} papers descargados')
    
    return textos