#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
# from flask_cors import CORS
from flask_wtf import CSRFProtect

from .config import Config
from app.utils.cache import configure_cache

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
# login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()
csrf = CSRFProtect()
# cors = CORS()


def create_app(config_class=Config):
    """
    Create a Flask application instance.
    :param config_class: Configuration class to use for the app.
    :return: Flask app instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize cache
    configure_cache(app)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    # login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)
    # cors.init_app(app)

    # Register blueprints
    from app.routes.main_routes import main_bp
    from app.routes.cultural_routes import cultural_bp
    from app.routes.contact_routes import contact_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(cultural_bp, url_prefix='/culture')
    app.register_blueprint(contact_bp)


    return app
