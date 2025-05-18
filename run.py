#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/run.py


from app import create_app
import os

app = create_app()

# This is the application object that Passenger uses
application = app

if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_HOST', '127.0.0.1'), 
            port=os.getenv('FLASK_PORT', 5000))
    