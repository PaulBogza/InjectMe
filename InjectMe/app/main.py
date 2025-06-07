from flask import Flask

from routes.login import login_routes
from routes.upload import upload_routes
from routes.home  import home_routes
from InjectMe.app.database.models import db_config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

app.register_blueprint(login_routes)
app.register_blueprint(upload_routes)
app.register_blueprint(home_routes)

if __name__ == '__main__':
   app.run(debug=True)