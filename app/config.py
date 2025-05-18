#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/config.py

import os
from dotenv import load_dotenv
from datetime import timedelta


class Config:
    """
    Base configuration class for the Flask application.
    """
    # Load environment variables from .env file
    load_dotenv()

    # General Config
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1']
    TESTING = os.getenv('TESTING', 'False').lower() in ['true', '1']
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = os.getenv('CSRF_SESSION_KEY', 'your_csrf_session_key')

    # Database Config
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail Config
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.example.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True').lower() in ['true', '1']
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', '')

    MAIL_DEFAULT_SENDER_NAME = os.getenv('MAIL_DEFAULT_SENDER_NAME', 'Swahili Jamboree')
    ERROR_ADMIN_EMAILS = os.getenv('ERROR_ADMIN_EMAILS', 'maintainance@swahilijamboree.org')
    
    # Logging configuration
    LOG_TO_STDOUT = os.getenv('LOG_TO_STDOUT', 'False').lower() in ['true', '1']
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
                                    
    # Cache Configuration
    CACHE_TYPE = os.getenv('CACHE_TYPE', 'simple')
    CACHE_TIMEOUT = int(os.getenv('CACHE_TIMEOUT', 21600))  # 6 hours
    CACHE_KEY_PREFIX = 'swahili_culture_'
    REDIS_URL = os.getenv('REDIS_URL', None)
    
    # CMS Configuration
    CMS_API_KEY = os.getenv('CMS_API_KEY')
    CMS_BASE_URL = os.getenv('CMS_BASE_URL')


