from typing import List
from sqlalchemy import String, Integer, Boolean, ForeignKey, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Sala(Base):
    __tablename__ = "salas"
    __table_args__ = (
        CheckConstraint("capacidad > 0", name="ck_capacidad_positiva"),
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    capacidad: Mapped[int] = mapped_column(Integer, nullable=False)
    disponible: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    reservas: Mapped[List["Reserva"]] = relationship(back_populates="sala")

    def __repr__(self) -> str:
        return f"Sala(id={self.id}, nombre={self.nombre}, disponible={self.disponible})"


class Reserva(Base):
    __tablename__ = "reservas"
    id: Mapped[int] = mapped_column(primary_key=True)
    estudiante: Mapped[str] = mapped_column(String(100), nullable=False)
    fecha: Mapped[str] = mapped_column(String(10), nullable=False)
    sala_id: Mapped[int] = mapped_column(ForeignKey("salas.id"), nullable=False)
    sala: Mapped["Sala"] = relationship(back_populates="reservas", lazy="joined")

    def __repr__(self) -> str:
        return f"Reserva(id={self.id}, estudiante={self.estudiante}, sala_id={self.sala_id})"