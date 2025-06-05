from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint

login_routes= Blueprint('login_routes', __name__, template_folder='templates')

@login_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return username
    if request.method == 'GET':
        return render_template('login.html')