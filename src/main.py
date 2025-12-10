# punto de entrada: menú principal (usuario/experto)
from interfaz_usuario import ejecutar_consulta
from interfaz_experto import ejecutar_editor


def main():
    while True:
        print("=== SISTEMA EXPERTO: Consultor de hardware ===")
        print("1. Modo usuario (obtener recomendación)")
        print("2. Modo experto (editar base de conocimientos)")
        print("0. Salir")
        opcion = input("Elija opción: ").strip()

        if opcion == "1":
            ejecutar_consulta()
        elif opcion == "2":
            ejecutar_editor()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.\n")


if __name__ == "__main__":
    main()
