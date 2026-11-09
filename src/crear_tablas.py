from conexion import engine
from modelos import Base

def crear_tablas():
    Base.metadata.create_all(engine)
    print("Tablas de salas y reservas creadas correctamente")

if __name__ == "__main__":
    crear_tablas()