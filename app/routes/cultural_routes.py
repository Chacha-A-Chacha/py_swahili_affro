#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/routes/cultural_routes.py


from flask import Blueprint, render_template, current_app, request
from app.services.cms_client import CMSClient
from app.utils.cache import cache

cultural_bp = Blueprint('cultural', __name__, template_folder='templates/cultural')
cms = CMSClient()

# Common cache timeout for cultural pages (1 hour)
CULTURAL_CACHE_TIMEOUT = 3600

@cultural_bp.route('/swahili-language')
@cache.cached(timeout=CULTURAL_CACHE_TIMEOUT)
def swahili_language():
    """Swahili language information page"""
    try:
        content = cms.get_content('swahili-language')
        return render_template('cultural/swahili_language.html',
                           hero=content.get('hero'),
                           lessons=content.get('lessons'),
                           resources=content.get('resources'))
    except Exception as e:
        current_app.logger.error(f"Swahili Language page error: {str(e)}")
        return render_template('cultural/swahili_language.html',
                           error=True)

@cultural_bp.route('/music-dance')
@cache.cached(timeout=CULTURAL_CACHE_TIMEOUT)
def music_dance():
    """Traditional music and dance page"""
    try:
        content_type = 'music-dance'
        if request.args.get('region'):
            content_type += f"?region={request.args['region']}"
        
        content = cms.get_content(content_type)
        return render_template('cultural/music_dance.html',
                           performances=content.get('performances'),
                           instruments=content.get('instruments'),
                           regions=content.get('regions'))
    except Exception as e:
        current_app.logger.error(f"Music & Dance page error: {str(e)}")
        return render_template('cultural/music_dance.html',
                           error=True)

@cultural_bp.route('/swahili-food')
@cache.cached(timeout=1800)  # 30 minute cache for frequently updated content
def swahili_food():
    """Traditional cuisine and recipes page"""
    try:
        recipe_type = request.args.get('type', 'all')
        content = cms.get_content(f'swahili-food?type={recipe_type}')
        
        return render_template('cultural/swahili_food.html',
                           featured_recipes=content.get('featured'),
                           categories=content.get('categories'),
                           recipe_type=recipe_type)
    except Exception as e:
        current_app.logger.error(f"Swahili Food page error: {str(e)}")
        return render_template('cultural/swahili_food.html',
                           error=True)

@cultural_bp.route('/fashion')
@cache.cached(timeout=CULTURAL_CACHE_TIMEOUT)
def fashion():
    """Traditional clothing and fashion page"""
    try:
        content = cms.get_content('fashion')
        return render_template('cultural/fashion.html',
                           traditional_wear=content.get('traditional'),
                           modern_adaptations=content.get('modern'),
                           designers=content.get('designers'))
    except Exception as e:
        current_app.logger.error(f"Fashion page error: {str(e)}")
        return render_template('cultural/fashion.html',
                           error=True)

@cultural_bp.route('/heritage')
@cache.cached(timeout=86400)  # 24-hour cache for less changing content
def heritage():
    """Cultural heritage and historical sites page"""
    try:
        region_filter = request.args.get('region', 'all')
        content = cms.get_content(f'heritage?region={region_filter}')
        
        return render_template('cultural/heritage.html',
                           sites=content.get('sites'),
                           regions=content.get('regions'),
                           current_region=region_filter)
    except Exception as e:
        current_app.logger.error(f"Heritage page error: {str(e)}")
        return render_template('cultural/heritage.html',
                           error=True)