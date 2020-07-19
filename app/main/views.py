from flask import render_template
from . import main
from flask_login import login_required

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

