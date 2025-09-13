import os
import SQLALCHEMY_DATABASE_URI 

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///movies.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
