#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# File: py_swahili_afro/app/forms/get_involved_forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SelectField
from wtforms.validators import DataRequired, Email, Length


class VolunteerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    skills = TextAreaField('Skills/Experience', validators=[Length(max=500)])
    availability = SelectField('Availability', choices=[
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('event', 'Specific Events'),
        ('flexible', 'Flexible')
    ])
