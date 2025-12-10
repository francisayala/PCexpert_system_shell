# Sistema Experto: Consultor de Hardware

Proyecto académico de sistema experto para recomendar equipos de cómputo
(PC/portátil) según propósito de uso, presupuesto y movilidad.

## Estructura del proyecto

- `src/` código fuente
  - `main.py` punto de entrada (menú principal)
  - `interfaz_usuario.py` modo usuario (consultas)
  - `interfaz_experto.py` modo experto (editor de reglas)
  - `motor_inferencia.py` motor de inferencia basado en reglas
  - `base_conocimientos.py` lectura/escritura de la base de conocimientos
  - `modelos.py` modelos de datos (Regla, etc.)
- `data/reglas.json` base de conocimientos (reglas en formato JSON)

## Cómo ejecutar

1. Abrir el proyecto en PyCharm.
2. Ejecutar `main.py` (Run → Run 'main').
3. Elegir:
   - Modo usuario para obtener recomendaciones.
   - Modo experto para editar reglas.
