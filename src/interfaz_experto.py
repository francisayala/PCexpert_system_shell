# menú para crear/editar/eliminar reglas
from typing import List

from base_conocimientos import (
    cargar_reglas,
    guardar_reglas,
    obtener_nueva_id,
    buscar_regla_por_id,
)
from modelos import Regla


def mostrar_reglas(reglas: List[Regla]) -> None:
    if not reglas:
        print("No hay reglas registradas.")
        return
    for r in reglas:
        print(f"\nID: {r.id}")
        print(f"  Condiciones: {r.condiciones}")
        print(f"  Recomendación: {r.recomendacion}")


def crear_regla(reglas: List[Regla]) -> None:
    print("\n=== CREAR NUEVA REGLA ===")
    proposito = input("proposito (juegos/oficina/estudio/...): ").strip().lower()
    presupuesto = input("presupuesto (bajo/medio/alto): ").strip().lower()
    movilidad = input("movilidad (escritorio/portatil): ").strip().lower()

    tipo = input("Tipo de dispositivo recomendado (texto): ").strip()
    config = input("Descripción de configuración (texto): ").strip()
    marcas_str = input("Marcas recomendadas (separadas por coma): ").strip()
    marcas = [m.strip() for m in marcas_str.split(",") if m.strip()]

    nueva_id = obtener_nueva_id(reglas)
    condiciones = {
        "proposito": proposito,
        "presupuesto": presupuesto,
        "movilidad": movilidad,
    }
    recomendacion = {
        "tipo": tipo,
        "config": config,
        "marcas": marcas,
    }
    regla = Regla(id=nueva_id, condiciones=condiciones, recomendacion=recomendacion)
    reglas.append(regla)
    guardar_reglas(reglas)
    print(f"Regla creada con ID {nueva_id}.")


def editar_regla(reglas: List[Regla]) -> None:
    try:
        id_str = input("ID de la regla a editar: ").strip()
        id_regla = int(id_str)
    except ValueError:
        print("ID inválido.")
        return

    regla = buscar_regla_por_id(reglas, id_regla)
    if not regla:
        print("No se encontró una regla con ese ID.")
        return

    print(f"Editando regla {id_regla}. Deje vacío para mantener el valor actual.")
    proposito = input(f"proposito actual={regla.condiciones.get('proposito')}: ").strip().lower()
    presupuesto = input(f"presupuesto actual={regla.condiciones.get('presupuesto')}: ").strip().lower()
    movilidad = input(f"movilidad actual={regla.condiciones.get('movilidad')}: ").strip().lower()

    tipo = input(f"tipo actual={regla.recomendacion.get('tipo')}: ").strip()
    config = input(f"config actual={regla.recomendacion.get('config')}: ").strip()
    marcas_str = input("marcas actuales (separadas por coma, vacío=mantener): ").strip()

    if proposito:
        regla.condiciones["proposito"] = proposito
    if presupuesto:
        regla.condiciones["presupuesto"] = presupuesto
    if movilidad:
        regla.condiciones["movilidad"] = movilidad
    if tipo:
        regla.recomendacion["tipo"] = tipo
    if config:
        regla.recomendacion["config"] = config
    if marcas_str:
        marcas = [m.strip() for m in marcas_str.split(",") if m.strip()]
        regla.recomendacion["marcas"] = marcas

    guardar_reglas(reglas)
    print("Regla actualizada.")


def eliminar_regla(reglas: List[Regla]) -> None:
    try:
        id_str = input("ID de la regla a eliminar: ").strip()
        id_regla = int(id_str)
    except ValueError:
        print("ID inválido.")
        return

    regla = buscar_regla_por_id(reglas, id_regla)
    if not regla:
        print("No se encontró una regla con ese ID.")
        return

    reglas.remove(regla)
    guardar_reglas(reglas)
    print("Regla eliminada.")


def ejecutar_editor() -> None:
    while True:
        print("\n=== MODO EXPERTO: Editor de base de conocimientos ===")
        print("1. Ver reglas")
        print("2. Crear nueva regla")
        print("3. Editar regla")
        print("4. Eliminar regla")
        print("0. Volver al menú principal")
        opcion = input("Elija opción: ").strip()

        reglas = cargar_reglas()

        if opcion == "1":
            mostrar_reglas(reglas)
        elif opcion == "2":
            crear_regla(reglas)
        elif opcion == "3":
            editar_regla(reglas)
        elif opcion == "4":
            eliminar_regla(reglas)
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")
