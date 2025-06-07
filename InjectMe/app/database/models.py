from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer
from sqlalchemy.orm import DecalrativebBase
from sqlalchemy.orm import mapped_collum 
from main import db

class User(db.Model):
    __tablename__ = "user"

    id = mapped_collum(Integer, primary_key = True)
    email = mapped_collum(String(100), nullable = False)
    username = mapped_collum(String(50), nullable = False)
    password = mapped_collum(String(100), nullable = False)

