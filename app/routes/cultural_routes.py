#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/routes/main_routes.py


from flask import Blueprint, render_template, request, redirect, url_for, flash


cultural_bp = Blueprint('cultural', __name__, template_folder='templates/cultural')
