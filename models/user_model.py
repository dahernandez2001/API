from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import declarative_base
from db import base 


class user():
    _tablename__ - "user"
    id - Column(Integer, primary_key-True, index-True)
    username - Column(String(50), unique-True, index-True, nullable-False)
    password - Column(String(255),nullable-False)