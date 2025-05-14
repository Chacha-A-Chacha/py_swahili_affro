#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/forms/contact_forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SelectField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    subject = SelectField('Subject', choices=[
        ('general', 'General Inquiry'),
        ('events', 'Events & Registration'),
        ('membership', 'Membership Information'),
        ('partnership', 'Partnership & Collaboration'),
        ('media', 'Media & Press'),
        ('cultural', 'Cultural Resources')
    ], validators=[DataRequired()])
    message = TextAreaField('Message', validators=[
        DataRequired(),
        Length(min=10, max=2000)
    ])
