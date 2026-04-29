"""
processors
==========
Subpaquete de procesamiento, limpieza y cálculo de métricas.

Módulos disponibles:
    cleaner: Limpieza y imputación del dataset crudo de PBDB.
"""

from .cleaner import imputar_entorno_dieta, limpiar_pantheria
from .merger import merge_data
from .enricher import enriquecer_modernos, imputar_dieta_modernos
from .manual_masses import MASAS_MANUALES