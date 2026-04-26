"""
collectors
==========
Subpackage de recolección de datos desde fuentes externas.

Módulos disponibles:
    pbdb: Paleobiology Database — megadepredadores fósiles.
"""
from .pbdb import obtener_todos
from .pantheria import obtener_modernos
from .eltontraits import obtener_modernos_aves