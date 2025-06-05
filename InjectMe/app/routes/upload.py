from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint

upload_routes = Blueprint('upload_routes', __name__, template_folder='templates')

@upload_routes.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('/home/nero/Code/InjectMe/app/uploads/' + f.filename)
    return render_template('upload.html')

