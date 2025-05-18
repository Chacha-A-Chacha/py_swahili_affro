#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/forms/contact_forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SelectField, TelField
from wtforms.validators import DataRequired, Email, Length, Optional

class ContactForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = EmailField('Email Address', validators=[DataRequired(), Email()])
    phone = TelField('Phone Number', validators=[Optional(), Length(max=20)])
    inquiry_type = SelectField('Inquiry Type', choices=[
        ('general', 'General Inquiry'),
        ('events', 'Events & Registration'),
        ('membership', 'Membership Information'),
        ('partnership', 'Partnership & Collaboration'),
        ('media', 'Media & Press'),
        ('cultural', 'Cultural Resources')
    ], validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=2, max=100)])
    message = TextAreaField('Message', validators=[
        DataRequired(),
        Length(min=10, max=2000)
    ])
