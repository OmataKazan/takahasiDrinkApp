#views.py
from flask import request,render_template,redirect,url_for,flash,Blueprint
from flaskr import db

bp=Blueprint('app',__name__,url_prefix='')

@bp.route('/')
def home():
    return render_template('home.html')