"""
rag/indexer.py
==============
Módulo para indexar abstracts científicos en ChromaDB
usando embeddings de sentence-transformers.

Convierte el texto de cada paper en vectores numéricos
que permiten búsqueda semántica por similitud.
"""

import chromadb
from sentence_transformers import SentenceTransformer

def inicializar_db(ruta: str = "data/vectordb") -> chromadb.Collection:
    """
    Inicializa la base de datos y guarda los embeddings en disco.

    Args:
        ruta: Ruta de donde guardar los embeddings.

    Returns:
        Base de datos de chromaDB.
    """
    cliente = chromadb.PersistentClient(path=ruta)
    coleccion = cliente.get_or_create_collection(name="papers_predadores")
    return coleccion

modelo = SentenceTransformer('all-MiniLM-L6-v2')

def indexar_textos(coleccion, especie: str, textos: list[str]) -> None:
    """
    Indexa los abstracts de una especie en ChromaDB.

    Args:
        coleccion: Colección de ChromaDB donde guardar los embeddings.
        especie: Nombre científico de la especie.
        textos: Lista de abstracts descargados de PubMed.
    """
    
    for i, texto in enumerate(textos):
        embedding = modelo.encode(texto).tolist()
        coleccion.add(
            documents=[texto],
            embeddings=[embedding],
            ids=[f"{especie}_{i}"],
            metadatas=[{"especie": especie}]
        )
    
    print(f'  {especie}: {len(textos)} abstracts indexados')