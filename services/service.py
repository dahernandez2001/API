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
