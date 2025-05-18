#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/routes/main_routes.py


from flask import Blueprint, render_template, request, redirect, url_for, flash

contact_bp = Blueprint('contact', __name__, template_folder='templates/contact')


from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from app.services.cms_client import CMSClient
import logging

from app.forms.contact_forms import ContactForm
from app.forms.get_involved_forms import VolunteerForm

contact_bp = Blueprint('contact', __name__)

# Form classes


@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page displaying a form and office locations."""
    form = ContactForm()
    cms = CMSClient()
    
    try:
        # Get content from CMS
        page_content = cms.get_content('contact-page')
        
        # If no content is available or error occurs, provide default structure
        if not page_content:
            page_content = {
                'hero': {
                    'title': 'Contact Us',
                    'subtitle': 'Get in Touch with Our Team',
                    'description': 'Have questions about Swahili Afro Jamboree or want to get involved? We\'d love to hear from you.',
                    'background_image': None
                },
                'intro': {
                    'title': 'We\'re Here to Help',
                    'description': 'Whether you have questions about our events, want to learn more about Swahili culture, or are interested in collaborating with us, our team is ready to assist you.'
                },
                'faqs': [
                    {
                        'question': 'What is the best way to reach your organization?',
                        'answer': 'Email is the most reliable way to reach us for non-urgent matters. For time-sensitive inquiries, please call our office during business hours. We aim to respond to all emails within 2 business days.'
                    },
                    {
                        'question': 'Can I visit your offices in person?',
                        'answer': 'Yes, our offices in Maryland, USA and Dar es Salaam, Tanzania welcome visitors during regular business hours. We recommend scheduling an appointment in advance to ensure the appropriate team members are available to assist you.'
                    },
                    {
                        'question': 'How can I get involved as a volunteer?',
                        'answer': 'We welcome volunteer support! Please use our contact form to express your interest, selecting \'Membership Information\' as the inquiry type, and mentioning your specific areas of interest or expertise. Our volunteer coordinator will reach out with opportunities.'
                    },
                    {
                        'question': 'Who should I contact regarding media inquiries or interview requests?',
                        'answer': 'For all media inquiries, press information, or interview requests, please select \'Media & Press\' in our contact form or email us directly with \'Media Inquiry\' in the subject line. Our communications team will respond promptly.'
                    }
                ],
                'offices': {
                    'northAmerica': {
                        'title': 'North America Office',
                        'address': [
                            'Registered Office, Swahili Afro Jamboree',
                            '6208 Alan Linton BLVD W',
                            'Fredrick, Maryland 21703, USA'
                        ],
                        'phone': '+1 240 614 1598',
                        'whatsapp': '+1 240 614 1598',
                        'email': 'pmabby@gmail.com',
                        'hours': 'Monday - Friday: 9:00 AM - 5:00 PM (EST)',
                        'mapUrl': 'https://maps.google.com'
                    },
                    'africa': {
                        'title': 'Africa Office',
                        'address': [
                            '8TH Floor Salamanda towers [GSM Building]',
                            'Samora avenue',
                            'P.o. Box 90342, Dar es Salaam, Tanzania'
                        ],
                        'phone': '+255 764 114 444',
                        'whatsapp': '+255 764 114 444',
                        'email': 'piimswaz@gmail.com',
                        'hours': 'Monday - Friday: 9:00 AM - 5:00 PM (EAT)',
                        'mapUrl': 'https://maps.google.com'
                    }
                }
            }
    except Exception as e:
        current_app.logger.error(f"Contact page CMS error: {str(e)}")
        page_content = None

    if form.validate_on_submit():
        try:
            # Process form data
            contact_data = {
                'name': form.name.data,
                'email': form.email.data,
                'phone': form.phone.data,
                'inquiry_type': form.inquiry_type.data,
                'subject': form.subject.data,
                'message': form.message.data
            }
            
            # TODO: Add integration with CMS API or email service
            # Example: cms.submit_form('contact', contact_data)
            
            current_app.logger.info(f"Contact form submission: {contact_data['email']}")
            flash('Your message has been sent successfully! We\'ll get back to you soon.', 'success')
            return redirect(url_for('contact.contact'))
        
        except Exception as e:
            current_app.logger.error(f"Contact form submission error: {str(e)}")
            flash('An error occurred while sending your message. Please try again later.', 'danger')

    return render_template('contact/contact.html',
                          form=form,
                          page_content=page_content)

@contact_bp.route('/get-involved', methods=['GET', 'POST'])
def get_involved():
    """Get involved page for volunteering and participation."""
    # This route implementation remains the same as before
    form = VolunteerForm()
    cms = CMSClient()
    
    try:
        opportunities = cms.get_content('volunteer-opportunities')
        page_content = cms.get_content('get-involved-page')
    except Exception as e:
        current_app.logger.error(f"Get Involved CMS error: {str(e)}")
        opportunities = None
        page_content = None

    if form.validate_on_submit():
        try:
            volunteer_data = {
                'name': form.name.data,
                'email': form.email.data,
                'skills': form.skills.data,
                'availability': form.availability.data
            }
            
            # TODO: Add integration with CMS API or database
            # Example: cms.submit_form('volunteer', volunteer_data)
            
            flash('Thank you for your interest! We\'ll be in touch soon.', 'success')
            return redirect(url_for('contact.get_involved'))
        
        except Exception as e:
            current_app.logger.error(f"Volunteer form submission error: {str(e)}")
            flash('An error occurred while processing your submission.', 'danger')

    return render_template('contact/get_involved.html',
                         form=form,
                         opportunities=opportunities,
                         page_content=page_content)

