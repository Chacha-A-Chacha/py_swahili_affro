#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/routes/main_routes.py

from flask import Blueprint, render_template, current_app
from app.services.cms_client import CMSClient
from app.utils.cache import cache

main_bp = Blueprint('main', __name__, template_folder='templates/main')

cms = CMSClient()

@main_bp.route('/')
@cache.cached(timeout=300)  # Cache homepage for 5 minutes
def home():
    """Home page with dynamic content from CMS"""
    try:
        content = cms.get_content('home')
        return render_template('main/home.html', 
                           hero_content=content.get('hero'),
                           featured=content.get('featured_sections'))
    except Exception as e:
        current_app.logger.error(f"Homepage error: {str(e)}")
        return render_template('main/home.html', 
                           hero_content=None,
                           featured=None)

@main_bp.route('/about')
def about():
    """Static about page with CMS-powered team section"""
    try:
        team_data = cms.get_content('team')
        return render_template('main/about.html', team=team_data)
    except Exception as e:
        current_app.logger.error(f"About page error: {str(e)}")
        return render_template('main/about.html', team=None)

@main_bp.route('/events')
@cache.cached(timeout=180)  # Cache events for 3 minutes
def events():
    """Events listing page with pagination"""
    try:
        events_data = cms.get_content('events')
        return render_template('main/events.html', 
                           upcoming_events=events_data.get('upcoming'),
                           past_events=events_data.get('past'))
    except Exception as e:
        current_app.logger.error(f"Events page error: {str(e)}")
        return render_template('main/events.html', 
                           upcoming_events=None,
                           past_events=None)

@main_bp.route('/news')
@cache.cached(timeout=300, query_string=True)  # Cache different pages
def news():
    """News articles with pagination and filtering"""
    try:
        page = request.args.get('page', 1, type=int)
        category = request.args.get('category', None)
        
        news_data = cms.get_content(f'news?page={page}&category={category}')
        
        return render_template('main/news.html',
                           articles=news_data.get('articles'),
                           current_page=page,
                           total_pages=news_data.get('total_pages'),
                           category=category)
    except Exception as e:
        current_app.logger.error(f"News page error: {str(e)}")
        return render_template('main/news.html', 
                           articles=None,
                           error_message="Failed to load news")

@main_bp.route('/media')
@cache.cached(timeout=3600)
def media():
    """Media gallery page with filtering"""
    try:
        media_type = request.args.get('type', 'all')
        media_data = cms.get_content(f'media?type={media_type}')
        
        return render_template('main/media.html',
                           media_items=media_data.get('items'),
                           media_type=media_type,
                           categories=media_data.get('categories'))
    except Exception as e:
        current_app.logger.error(f"Media page error: {str(e)}")
        return render_template('main/media.html',
                           media_items=None,
                           error=True)