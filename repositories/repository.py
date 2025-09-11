from models.director import Director
from app import db

class DirectorRepository:
    def get_all(self):
        return Director.query.all()

    def get_by_id(self, id_):
        return Director.query.get(id_)

    def create(self, name):
        director = Director(name=name)
        db.session.add(director)
        db.session.commit()
        return director

    def update(self, id_, name):
        director = self.get_by_id(id_)
        if director:
            director.name = name
            db.session.commit()
        return director

    def delete(self, id_):
        director = self.get_by_id(id_)
        if director:
            db.session.delete(director)
            db.session.commit()
        return director
