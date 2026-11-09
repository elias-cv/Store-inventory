from sqlalchemy import select
from conexion import Session
from modelos import Reserva, Sala

def registrar_reserva(estudiante: str, sala_id: int, fecha: str):
    if not estudiante or not estudiante.strip():
        raise ValueError("El nombre del estudiante debe contener caracteres y es obligatorio.")
    with Session.begin() as session:
        sala = session.get(Sala, sala_id)

        if sala is None:
            raise ValueError(f"No existe una sala con el ID ingresado{sala_id}.")

        if not sala.disponible:
            raise ValueError(f"Error: la sala '{sala.nombre}' ya se encuentra ocupada, no esta disponible.")

        sala.disponible = False
        nueva_reserva = Reserva(
            estudiante=estudiante.strip(),
            sala_id=sala.id,
            fecha=fecha.strip()
        )
        session.add(nueva_reserva)
        return nueva_reserva


def consultar_reservas():
    with Session() as session:
        reserva = select(Reserva)
        return session.scalars(reserva).all()


def cancelar_reserva(id_reserva: int):
    with Session.begin() as session:
        reserva = session.get(Reserva, id_reserva)

        if reserva is None:
            raise ValueError(f"Error: no existe ninguna reserva con ID ingresado {id_reserva}.")

        sala = session.get(Sala, reserva.sala_id)
        if sala:
            sala.disponible = True

        session.delete(reserva)
        return True