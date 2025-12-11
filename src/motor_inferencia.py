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

    def inferir_con_traza(
            self, hechos: Dict[str, Any]
    ) -> Tuple[List[Tuple[Regla, Dict[str, Any]]], List[str]]:
        """
        Versión con traza detallada del proceso de razonamiento.
        Devuelve:
          - lista de (regla, recomendacion) disparadas
          - lista de líneas de texto con la explicación paso a paso
        """
        traza: List[str] = []

        # Paso 1: hechos iniciales
        traza.append("PASO 1: El sistema recibe los datos introducidos por el usuario:")
        traza.append(f"  Hechos iniciales = {hechos}")

        # Paso 2: carga de reglas
        num_reglas = len(self.reglas)
        traza.append("PASO 2: Se cargan las reglas de la base de conocimientos (modelo de producción).")
        traza.append(f"  Número total de reglas = {num_reglas}")

        resultados: List[Tuple[Regla, Dict[str, Any]]] = []

        # Paso 3: ciclo de emparejamiento (match) y disparo (fire) de reglas
        traza.append("PASO 3: El motor de inferencia recorre todas las reglas y comprueba sus condiciones:")

        for regla in self.reglas:
            traza.append(f"- Analizando regla #{regla.id} con condiciones {regla.condiciones}")
            coincide_todo = True

            for atributo, valor_regla in regla.condiciones.items():
                valor_usuario = hechos.get(atributo)
                if valor_usuario == valor_regla:
                    traza.append(
                        f"    · Coincidencia en '{atributo}': "
                        f"usuario = '{valor_usuario}', regla = '{valor_regla}'"
                    )
                else:
                    traza.append(
                        f"    · NO coincide '{atributo}': "
                        f"usuario = '{valor_usuario}', regla = '{valor_regla}'"
                    )
                    coincide_todo = False

            if coincide_todo:
                traza.append(f"    ⇒ Todas las condiciones se cumplen: la regla #{regla.id} SE DISPARA.")
                resultados.append((regla, regla.recomendacion))
            else:
                traza.append(f"    ⇒ No se cumplen todas las condiciones: la regla #{regla.id} NO se dispara.")

        # Paso 4: conclusión
        if not resultados:
            traza.append("PASO 4: Ninguna regla se ha disparado. No hay una recomendación exacta para estos datos.")
        else:
            traza.append(
                f"PASO 4: Se han disparado {len(resultados)} regla(s). "
                "Estas reglas generan las recomendaciones finales que se muestran al usuario."
            )

        return resultados, traza

    @staticmethod
    def _coincide(regla: Regla, hechos: Dict[str, Any]) -> bool:
        for atributo, valor in regla.condiciones.items():
            if hechos.get(atributo) != valor:
                return False
        return True
