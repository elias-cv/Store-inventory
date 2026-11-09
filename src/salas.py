from sqlalchemy import select
from conexion import Session
from modelos import Sala

def insertar_sala(nombre: str, capacidad: int):
    if not nombre or not nombre.strip():
        raise ValueError("El nombre de la sala no puede estar vacío.")

    if capacidad <= 0:
        raise ValueError("La capacidad debe ser mayor que cero.")

    with Session.begin() as session:
        nueva_sala = Sala(nombre=nombre.strip(), capacidad=capacidad, disponible=True)
        session.add(nueva_sala)
        return nueva_sala

def consultar_salas():
    with Session() as session:
        stmt = select(Sala)
        salas = session.scalars(stmt).all()
        return salas