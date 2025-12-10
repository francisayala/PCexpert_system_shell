# clases auxiliares: Regla, Hechos, etc.
from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class Regla:
    id: int
    condiciones: Dict[str, Any]
    recomendacion: Dict[str, Any]


def regla_desde_dict(data: Dict[str, Any]) -> Regla:
    return Regla(
        id=data["id"],
        condiciones=data["condiciones"],
        recomendacion=data["recomendacion"],
    )


def regla_a_dict(regla: Regla) -> Dict[str, Any]:
    return {
        "id": regla.id,
        "condiciones": regla.condiciones,
        "recomendacion": regla.recomendacion,
    }
