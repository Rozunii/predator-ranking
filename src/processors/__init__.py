"""
processors
==========
Subpaquete de procesamiento, limpieza y cálculo de métricas.

Módulos disponibles:
    cleaner: Limpieza y imputación del dataset crudo de PBDB.
"""

from .cleaner import eliminar_duplicados, imputar_entorno