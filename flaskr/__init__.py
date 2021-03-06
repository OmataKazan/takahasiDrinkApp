#__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__name__))
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aefacregadfaerfrgl'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    from flaskr.views import bp
    app.register_blueprint(bp)
    from flaskr.views import bp
    app.register_blueprint(bp)
    return app