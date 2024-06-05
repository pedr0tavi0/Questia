from sqlalchemy import inspect
import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_bcrypt import Bcrypt
from sqlalchemy_utils import database_exists, create_database
from config import Config
import logging

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'pedro'


    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    if not database_exists(db_uri):
        create_database(db_uri)
 
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
         from.models.user import User
         db.create_all()
    


    

    from app.controllers import auth_controller, main_controller, questionario_controller
    app.register_blueprint(auth_controller.bp)
    app.register_blueprint(main_controller.bp)
    app.register_blueprint(questionario_controller.bp)

   

    return app
