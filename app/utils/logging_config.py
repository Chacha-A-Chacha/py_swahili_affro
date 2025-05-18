#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# File: py_swahili_afro/app/utils/logging_config.py

import os
import logging
from logging.handlers import RotatingFileHandler, SMTPHandler
from flask import Flask, request

def configure_logging(app: Flask):
    """
    Configure logging for the application.
    
    Sets up:
    1. Console logging
    2. Rotating file logs (separate for access and error)
    3. Email notifications for errors
    
    :param app: Flask application instance
    """
    # Create logs directory if it doesn't exist
    logs_dir = os.path.join(app.root_path, '..', 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    
    # Configure basic logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Configure access log file handler
    access_log = os.path.join(logs_dir, 'access.log')
    access_file_handler = RotatingFileHandler(
        access_log, 
        maxBytes=10485760,  # 10MB
        backupCount=10
    )
    access_file_handler.setLevel(logging.INFO)
    access_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(remote_addr)s - %(method)s %(path)s %(status)s - %(message)s'
    ))
    
    # Configure error log file handler
    error_log = os.path.join(logs_dir, 'error.log')
    error_file_handler = RotatingFileHandler(
        error_log, 
        maxBytes=10485760,  # 10MB
        backupCount=10
    )
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s\n'
        'Path: %(path)s\n'
        'Method: %(method)s\n'
        'Remote Address: %(remote_addr)s\n'
        '%(exc_info)s'
    ))
    
    # Email error handler for critical errors
    if not app.debug and app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] and app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
            
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr=app.config['MAIL_DEFAULT_SENDER'],
            toaddrs=app.config['ERROR_ADMIN_EMAILS'].split(','),
            subject='Swahili Afro Jamboree: Application Error',
            credentials=auth,
            secure=secure
        )
        mail_handler.setLevel(logging.ERROR)
        mail_handler.setFormatter(logging.Formatter(
            '''
            Time: %(asctime)s
            Message: %(message)s
            Path: %(path)s
            Method: %(method)s
            Remote Address: %(remote_addr)s
            
            %(exc_info)s
            '''
        ))
        app.logger.addHandler(mail_handler)
    
    # Add filter to include request info
    class RequestInfoFilter(logging.Filter):
        def filter(self, record):
            record.path = request.path if request else "No request context"
            record.method = request.method if request else "No request context"
            record.remote_addr = request.remote_addr if request else "No request context"
            record.exc_info = record.exc_info or ""
            return True
            
    request_filter = RequestInfoFilter()
    access_file_handler.addFilter(request_filter)
    error_file_handler.addFilter(request_filter)
    
    # Add handlers to app logger
    app.logger.addHandler(access_file_handler)
    app.logger.addHandler(error_file_handler)
    
    # Set app logger level
    app.logger.setLevel(logging.INFO)
    
    # Log application startup
    # app.logger.info(f"Swahili Afro Jamboree application started in {app.config['ENV']} mode")
