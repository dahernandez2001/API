import os
from models.models import pelicula, director
from sqlalchemy.orm import session


def __init__(self, db_session: session):
    self.db = db_session

def get_all_libros(self):
    return self.db.query(pelicula).all()

def get_libro_by_id(self, pelicula_id: int):
    return self.db.query(pelicula).filter(pelicula.id == pelicula_id).first()

def create_libro(self, name: str):
    nuevo_pelicula = pelicula(name=name)
    self.db.add(nuevo_pelicula)
    self.db.commit()
    self.db.refresh(nuevo_pelicula)
    return nuevo_pelicula


def actualizar_libro(selft,pelicula_id: id, name:str = None):
    pelicula = selft.get_pelicula_by_id(pelicula_id)
    if pelicula and name:
        pelicula.name = name
        selft.db.commit()
        selft.db.refresh(pelicula)
    return pelicula


def eliminar_banda(self, pelicula_id: int):
    pelicula = self.get_pelicula_by_id(pelicula_id)
    if pelicula:
        self.db.delete(pelicula)
        self.db.commit()
    return pelicula