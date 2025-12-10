# carga/guarda y edición de reglas (BK)
import json
from pathlib import Path
from typing import List, Optional

from modelos import Regla, regla_desde_dict, regla_a_dict



RUTA_BK = Path(__file__).resolve().parents[1] / "data" / "reglas.json"


def cargar_reglas() -> List[Regla]:
    if not RUTA_BK.exists():
        return []
    with open(RUTA_BK, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [regla_desde_dict(r) for r in data]


def guardar_reglas(reglas: List[Regla]) -> None:
    data = [regla_a_dict(r) for r in reglas]
    with open(RUTA_BK, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def obtener_nueva_id(reglas: List[Regla]) -> int:
    if not reglas:
        return 1
    return max(r.id for r in reglas) + 1


def buscar_regla_por_id(reglas: List[Regla], id_buscar: int) -> Optional[Regla]:
    for r in reglas:
        if r.id == id_buscar:
            return r
    return None
