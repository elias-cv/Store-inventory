from crear_tablas import crear_tablas
from salas import insertar_sala, consultar_salas
from reservas import registrar_reserva, consultar_reservas, cancelar_reserva

def mostrar_menu():
    print("\n" + "=" * 45)
    print("--SISTEMA DE RESERVAS DE SALAS DE ESTUDIO--")
    print("=" * 45)
    print("1. Registrar sala")
    print("2. Consultar salas")
    print("3. Registrar reserva")
    print("4. Consultar reservas")
    print("5. Cancelar reserva")
    print("0. Salir")
    print("=" * 45)


def main_registrar_sala():
    print("\n--- Registrar Sala ---")
    nombre = input("Nombre de la sala: ").strip()
    try:
        capacidad = int(input("Capacidad de personas: "))
        sala = insertar_sala(nombre, capacidad)
        print(f"Éxito: Sala '{sala.nombre}' creada con ID {sala.id} (Disponible: {sala.disponible})")
    except ValueError as e:
        print(f"Error de validación: {e}")


def main_consultar_salas():
    print("\n--- Lista de Salas ---")
    salas = consultar_salas()
    
    if not salas:
        print("No hay salas registradas.")
        return

    for s in salas:
        estado = "Disponible" if s.disponible else "Ocupada"
        print(f"ID: {s.id} | Sala: {s.nombre} | Capacidad: {s.capacidad} | Estado: {estado}")

def main_registrar_reserva():
    print("\n--- Registrar Reserva ---")
    estudiante = input("Nombre del estudiante: ").strip()
    fecha = input("Fecha : ").strip()
    try:
        sala_id = int(input("ID de la sala: "))
        reserva = registrar_reserva(estudiante, sala_id, fecha)
        print(f"Reserva registrada con éxito para {reserva.estudiante} en la sala ID {reserva.sala_id}")
    except ValueError as e:
        print(f"Error: {e}")

def main_consultar_reservas():
    print("\n--- Lista de Reservas Activas ---")
    reservas = consultar_reservas()

    if not reservas:
        print("No existen reservas registradas.")
        return

    for r in reservas:
        print(f"ID: {r.id} | Estudiante: {r.estudiante} | Sala: {r.sala.nombre} | Fecha: {r.fecha}")


def main_cancelar_reserva():
    print("\n--- Cancelar Reserva ---")
    try:
        id_reserva = int(input("ID de la reserva a cancelar: "))
        cancelar_reserva(id_reserva)
        print(f"Éxito: Reserva {id_reserva} cancelada y sala liberada correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    crear_tablas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            main_registrar_sala()
        elif opcion == "2":
            main_consultar_salas()
        elif opcion == "3":
            main_registrar_reserva()
        elif opcion == "4":
            main_consultar_reservas()
        elif opcion == "5":
            main_cancelar_reserva()
        elif opcion == "0":
            print("\nCerrando el sistema.")
            break
        else:
            print("Opción inválida, ingrese un número del 0 al 5.")


if __name__ == "__main__":
    main()