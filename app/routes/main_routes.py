#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/routes/main_routes.py


from flask import Blueprint, render_template, request, redirect, url_for, flash


main_bp = Blueprint('main', __name__, template_folder='templates/main')
