"""
rag/extractor.py
================
Módulo para extraer datos específicos de papers científicos
usando recuperación semántica desde ChromaDB y un LLM.

Para cada especie recupera los fragmentos más relevantes
y extrae masa corporal, rango temporal y distribución geográfica
con cita incluida.
"""

import os
import chromadb
from sentence_transformers import SentenceTransformer
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

modelo = SentenceTransformer('all-MiniLM-L6-v2')

def recuperar_contexto(coleccion, especie: str, pregunta: str) -> str:
    """
    Recupera los fragmentos más relevantes de ChromaDB para una pregunta.

    Convierte la pregunta a embedding y busca los 3 abstracts
    más similares para la especie indicada.

    Args:
        coleccion: Colección de ChromaDB con los abstracts indexados.
        especie: Nombre científico de la especie a consultar.
        pregunta: Pregunta en lenguaje natural sobre la especie.

    Returns:
        String con los fragmentos más relevantes concatenados.
    """

    embedding = modelo.encode(pregunta).tolist()
    
    resultados = coleccion.query(
        query_embeddings=[embedding],
        n_results=3,
        where={"especie": especie}
    )
    
    textos = resultados['documents'][0]
    return "\n\n".join(textos)


def extraer_dato(especie: str, contexto: str, dato: str) -> str:
    """
    Extrae un dato específico de los abstracts usando un LLM.

    Args:
        especie: Nombre científico de la especie.
        contexto: Fragmentos de papers recuperados de ChromaDB.
        dato: Dato a extraer (ej. "masa corporal en kg").

    Returns:
        String con el dato extraído y la fuente si está disponible.
    """
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.3-70b-versatile"
    )

    prompt = f"""Eres un asistente científico especializado en paleontología y biología.
    
Dado el siguiente contexto de papers científicos sobre {especie}:

{contexto}

Extrae el siguiente dato: {dato}

Responde SOLO con el valor numérico y las unidades. Si no encuentras el dato responde: NO_ENCONTRADO.
Ejemplo de respuesta correcta: "8000 kg"
"""

    respuesta = llm.invoke(prompt)
    return respuesta.content


def extraer_masa_corporal(coleccion, especie: str) -> str:
    """
    Extrae la masa corporal de una especie usando RAG.

    Recupera contexto relevante de ChromaDB y usa un LLM
    para extraer la masa corporal con su unidad.

    Args:
        coleccion: Colección de ChromaDB con abstracts indexados.
        especie: Nombre científico de la especie.

    Returns:
        String con la masa corporal estimada o NO_ENCONTRADO.
    """
    contexto = recuperar_contexto(
        coleccion, 
        especie, 
        "body mass weight estimate kilograms tons"
    )
    
    return extraer_dato(especie, contexto, "masa corporal estimada en kg")