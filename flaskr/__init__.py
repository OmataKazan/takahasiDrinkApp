#__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__name__))
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
login_manager = LoginManager() #ログインマネージャ

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = b'\xa9\xfb\x81l\x8c\xe9\xa7\xcb\xb80\xcb02\xea\x9b\xb6'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    from flaskr.views import bp
    app.register_blueprint(bp)
    from flaskr.views import bp
    app.register_blueprint(bp)
    return app