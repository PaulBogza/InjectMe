from flask import Flask

from routes.login import login_routes
from routes.upload import upload_routes
from routes.home  import home_routes
from database.db import db_config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)

app.register_blueprint(db_config)
app.register_blueprint(login_routes)
app.register_blueprint(upload_routes)
app.register_blueprint(home_routes)

if __name__ == '__main__':
   app.run(debug=True)