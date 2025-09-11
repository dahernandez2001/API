class DirectorService:
    def __init__(self, repository):
        self.repo = repository

    def get_all(self):
        try:
            return self.repo.get_all()
        except Exception as e:
            print(f"Error fetching directors: {e}")
            return []

    def get_by_id(self, id_):
        try:
            return self.repo.get_by_id(id_)
        except Exception as e:
            print(f"Error fetching director {id_}: {e}")
            return None

    def create(self, name):
        try:
            return self.repo.create(name)
        except Exception as e:
            print(f"Error creating director: {e}")
            return None

    def update(self, id_, name):
        try:
            return self.repo.update(id_, name)
        except Exception as e:
            print(f"Error updating director {id_}: {e}")
            return None

    def delete(self, id_):
        try:
            return self.repo.delete(id_)
        except Exception as e:
            print(f"Error deleting director {id_}: {e}")
            return None

class MovieService:
    def __init__(self, movie_repo, director_repo):
        self.movie_repo = movie_repo
        self.director_repo = director_repo

    def get_all(self):
        try:
            return self.movie_repo.get_all()
        except Exception as e:
            print(f"Error fetching movies: {e}")
            return []

    def get_by_id(self, id_):
        try:
            return self.movie_repo.get_by_id(id_)
        except Exception as e:
            print(f"Error fetching movie {id_}: {e}")
            return None

    def create(self, title, year, director_id):
        try:
            if not self.director_repo.get_by_id(director_id):
                print(f"Director {director_id} not found")
                return None
            return self.movie_repo.create(title, year, director_id)
        except Exception as e:
            print(f"Error creating movie: {e}")
            return None

    def update(self, id_, title=None, year=None, director_id=None):
        try:
            if director_id and not self.director_repo.get_by_id(director_id):
                print(f"Director {director_id} not found")
                return None
            return self.movie_repo.update(id_, title, year, director_id)
        except Exception as e:
            print(f"Error updating movie {id_}: {e}")
            return None

    def delete(self, id_):
        try:
            return self.movie_repo.delete(id_)
        except Exception as e:
            print(f"Error deleting movie {id_}: {e}")
            return None
