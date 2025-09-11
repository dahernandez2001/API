from config.config import Config

class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    movies = db.relationship("Movie", backref="director", cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "name": self.name}

from app import db

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "director_id": self.director_id,
            "director_name": self.director.name if self.director else None,
        }
