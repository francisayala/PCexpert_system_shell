from typing import Dict, Any

from motor_inferencia import MotorInferencia


def elegir_opcion(mensaje: str, opciones: Dict[int, tuple]) -> str:
    """
    Muestra un menú numerado y devuelve el valor interno (clave lógica)
    asociado a la opción elegida.
    opciones: {numero: (valor_interno, texto_mostrado)}
    """
    while True:
        print()
        print(mensaje)
        for num, (valor, texto) in opciones.items():
            print(f"{num}. {texto}")
        eleccion = input("Elija una opción: ").strip()

        if eleccion.isdigit():
            num = int(eleccion)
            if num in opciones:
                return opciones[num][0]

        print("Opción no válida, intente de nuevo.")


def preguntar_usuario() -> Dict[str, Any]:
    print("=== CONSULTA: Asistente para elección de equipo ===")

    opciones_proposito = {
        1: ("juegos", "Juegos"),
        2: ("oficina", "Oficina / trabajo de oficina"),
        3: ("estudio", "Estudio / universidad"),
        4: ("video", "Edición de video / contenido"),
        5: ("otro", "Uso general / otro")
    }

    opciones_presupuesto = {
        1: ("bajo", "Bajo"),
        2: ("medio", "Medio"),
        3: ("alto", "Alto")
    }

    opciones_movilidad = {
        1: ("escritorio", "Sobremesa (PC de escritorio)"),
        2: ("portatil", "Portátil / laptop")
    }

    proposito = elegir_opcion(
        "¿Para qué usará el equipo?",
        opciones_proposito
    )

    presupuesto = elegir_opcion(
        "¿Cuál es su rango de presupuesto?",
        opciones_presupuesto
    )

    movilidad = elegir_opcion(
        "¿Qué tipo de equipo prefiere?",
        opciones_movilidad
    )

    hechos: Dict[str, Any] = {
        "proposito": proposito,
        "presupuesto": presupuesto,
        "movilidad": movilidad,
    }
    return hechos


def ejecutar_consulta() -> None:
    motor = MotorInferencia()
    hechos: Dict[str, Any] = preguntar_usuario()

    # Llamamos a la versión con traza
    resultados, traza = motor.inferir_con_traza(hechos)

    # Mostrar la traza completa del proceso de razonamiento
    print("\n=== TRAZA DEL PROCESO DE RAZONAMIENTO DEL SISTEMA EXPERTO ===")
    for linea in traza:
        print(linea)

    # Después, mostrar las recomendaciones finales
    if not resultados:
        print("\n=== RESULTADO FINAL ===")
        print("No se encontraron recomendaciones exactas para esos parámetros.")
        print("El motor de inferencia no encontró ninguna regla cuyas condiciones "
              "coincidan completamente con las respuestas dadas.\n")
        return

    print("\n=== RECOMENDACIONES FINALES GENERADAS POR LAS REGLAS DISPARADAS ===")
    for regla, recomendacion in resultados:
        print(f"\nRegla #{regla.id}")
        print(f"Tipo de dispositivo: {recomendacion.get('tipo')}")
        print(f"Configuración sugerida: {recomendacion.get('config')}")
        marcas = recomendacion.get("marcas", [])
        if marcas:
            print(f"Marcas recomendadas: {', '.join(marcas)}")

        # Explicación resumida de por qué esta regla en concreto se disparó
        print("\nExplicación específica de esta variante:")
        print("  Esta variante proviene de una regla de producción de la forma")
        print("  'SI (proposito, presupuesto, movilidad, ...) ENTONCES (recomendación)'.")
        print("  La regla #{} se disparó porque para todos sus atributos clave se cumplió:".format(regla.id))
        for atributo, valor_regla in regla.condiciones.items():
            valor_usuario = hechos.get(atributo)
            print(f"  - {atributo}: usted eligió '{valor_usuario}' "
                  f"y la regla exige '{valor_regla}'. (Coinciden)")

    print("\nEl sistema ha aplicado un modelo de producción con encadenamiento hacia adelante: "
          "partiendo de sus datos de entrada, ha recorrido todas las reglas, "
          "ha comprobado sus condiciones y ha activado aquellas que coincidían totalmente.\n")

