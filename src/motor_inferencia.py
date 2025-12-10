# clase MotorInferencia (forward chaining)
from typing import Dict, Any, List, Tuple

from base_conocimientos import cargar_reglas
from modelos import Regla


class MotorInferencia:
    """
    Motor de inferencia muy simple: forward chaining con coincidencia exacta
    de atributos (IF condiciones THEN recomendacion).
    """

    def __init__(self) -> None:
        self.reglas: List[Regla] = cargar_reglas()

    def recargar(self) -> None:
        """Vuelve a leer las reglas desde la base de conocimientos."""
        self.reglas = cargar_reglas()

    def inferir(self, hechos: Dict[str, Any]) -> List[Tuple[Regla, Dict[str, Any]]]:
        """
        Devuelve lista de (regla, recomendacion) que cumplen todas sus condiciones.
        """
        resultados: List[Tuple[Regla, Dict[str, Any]]] = []
        for regla in self.reglas:
            if self._coincide(regla, hechos):
                resultados.append((regla, regla.recomendacion))
        return resultados

    @staticmethod
    def _coincide(regla: Regla, hechos: Dict[str, Any]) -> bool:
        for atributo, valor in regla.condiciones.items():
            if hechos.get(atributo) != valor:
                return False
        return True
