from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column 
from main import db

class User(db.Model):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key = True)
    email = mapped_column(String(100), nullable = False)
    username = mapped_column(String(50), nullable = False)
    password = mapped_column(String(100), nullable = False)

    def __repr__(self):
        return '<User {}>'.format(self.username)
