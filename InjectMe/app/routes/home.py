from flask import Flask
from flask import request
from flask import Blueprint
from flask import render_template

home_routes = Blueprint('home', __name__, template_folder='templates')

@home_routes.route('/')
@home_routes.route('/<username>')
def home(username=None):
   return render_template('index.html', person=username)


