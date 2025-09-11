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

from models.movie import Movie
from app import db

class MovieRepository:
    def get_all(self):
        return Movie.query.all()

    def get_by_id(self, id_):
        return Movie.query.get(id_)

    def create(self, title, year, director_id):
        movie = Movie(title=title, year=year, director_id=director_id)
        db.session.add(movie)
        db.session.commit()
        return movie

    def update(self, id_, title=None, year=None, director_id=None):
        movie = self.get_by_id(id_)
        if movie:
            if title:
                movie.title = title
            if year:
                movie.year = year
            if director_id:
                movie.director_id = director_id
            db.session.commit()
        return movie

    def delete(self, id_):
        movie = self.get_by_id(id_)
        if movie:
            db.session.delete(movie)
            db.session.commit()
        return movie
