from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DecalrativebBase
from flask import Blueprint

db_config = Blueprint('db_config')

class Base(DecalrativebBase):
    pass

db = SQLAlchemy(model_class=Base)

db_config.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://db.db"
db.init_app(db_config)

