import os
basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    SECRET_KEY='dev'
    SQLALCHEMY_DATABASE_URI  = 'sqlite:////' + os.path.join(basedir ,'app.db')