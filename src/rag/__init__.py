"""
rag
===
Subpaquete de Retrieval-Augmented Generation para extracción
de datos paleontológicos desde literatura científica.

Módulos disponibles:
    fetcher: Descarga abstracts desde PubMed Central.
    indexer: Indexa abstracts en ChromaDB con embeddings.
    extractor: Extrae datos específicos usando LLM + ChromaDB.
"""

from .fetcher import obtener_textos
from .indexer import inicializar_db, indexar_textos
from .extractor import extraer_masa_corporal