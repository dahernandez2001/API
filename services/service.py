from repositories.pelicula import director
from models.pelicula import pelicula
from sqlalchemy.orm import session

class BandService:
    def __init__(self, db_session: session):
        self.repository = db_session

def listar_pelicula(self):
    return self.repository.get_all_pelicula()

def obtener_pelicula(self, pelicula_id: int):
    return self.repository.get_pelicula_by_id(pelicula_id)

def crear_pelicula(self, name: str):
    return self.repository.crear_pelicula(name)

def actualizar_pelicula(self, pelicula_id: int, name: str = None):
    return self.repository.actualuzar_pelicula(pelicula_id, name)

def eliminar_pelicula(self, pelicula_id: int):
    return self.repository.eliminar_pelicula(pelicula_id)