#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/__init__.py

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
# from flask_cors import CORS
from flask_wtf import CSRFProtect

from .config import Config
from app.utils.cache import configure_cache
from app.utils.logging_config import configure_logging


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

    # Configure logging
    configure_logging(app)

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

    # Register error handlers
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    """Register error handlers for the application."""
    
    @app.errorhandler(404)
    def not_found_error(error):
        app.logger.info(f"404 error: {error}")
        return render_template('errors/404.html'), 404
        
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()  # Roll back db session in case of error during transactions
        app.logger.error(f"500 error: {error}", exc_info=True)
        
        # Send email notification for 500 errors
        from app.utils.mail import send_error_notification
        send_error_notification(error)
        
        return render_template('errors/500.html'), 500