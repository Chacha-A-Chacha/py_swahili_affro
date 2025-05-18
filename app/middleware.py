#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/middleware.py

from flask import request, current_app
from time import time
import logging

class RequestLoggingMiddleware:
    """Middleware for logging requests."""
    
    def __init__(self, app):
        self.app = app
        self.app.before_request(self.before_request)
        self.app.after_request(self.after_request)
        
    def before_request(self):
        """Log before processing the request."""
        request.start_time = time()
        
    def after_request(self, response):
        """Log after processing the request."""
        request_time = round((time() - request.start_time) * 1000, 2)
        
        # Skip logging for static files
        if not request.path.startswith('/static') and not request.path.startswith('/favicon'):
            current_app.logger.info(
                f"Request completed in {request_time}ms - Status: {response.status_code}",
                extra={
                    'path': request.path,
                    'method': request.method,
                    'status': response.status_code,
                    'request_time_ms': request_time
                }
            )
        
        return response
    