#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/utils/mail.py

from flask import current_app, render_template
from flask_mail import Message
from app import mail
import threading

def send_async_email(app, msg):
    """Send email asynchronously."""
    with app.app_context():
        mail.send(msg)

def send_email(subject, recipients, template=None, html_body=None, text_body=None, **kwargs):
    """
    Send an email using the configured mail server.
    
    :param subject: Email subject
    :param recipients: List of recipient email addresses
    :param template: The template name (without extension) to use for rendering
    :param html_body: HTML content if not using a template
    :param text_body: Text content if not using a template
    :param kwargs: Template context variables
    :return: None
    """
    app = current_app._get_current_object()
    msg = Message(subject, recipients=recipients, 
                  sender=app.config['MAIL_DEFAULT_SENDER'])
    
    if template:
        msg.html = render_template(f'emails/{template}.html', **kwargs)
        msg.body = render_template(f'emails/{template}.txt', **kwargs)
    else:
        msg.html = html_body
        msg.body = text_body
    
    # Send email asynchronously
    threading.Thread(
        target=send_async_email,
        args=(app, msg)
    ).start()

def send_error_notification(error, context=None):
    """
    Send error notification to admin.
    
    :param error: Exception or error message
    :param context: Additional context information
    :return: None
    """
    app = current_app._get_current_object()
    recipients = app.config['ERROR_ADMIN_EMAILS'].split(',')
    
    if not recipients or not app.config['MAIL_SERVER']:
        app.logger.warning("Cannot send error notification: mail settings not configured")
        return
        
    context = context or {}
    error_details = {
        'error_message': str(error),
        'error_type': type(error).__name__,
        'additional_context': context
    }
    
    send_email(
        subject="[ALERT] Swahili Afro Jamboree Error",
        recipients=recipients,
        template='error_notification',
        error=error_details
    )
    