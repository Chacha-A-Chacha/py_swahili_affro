#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/utils/cache.py

from flask_caching import Cache
from datetime import timedelta

cache = Cache()

def configure_cache(app):
    """Configure cache settings"""
    cache_config = {
        'CACHE_TYPE': app.config.get('CACHE_TYPE', 'simple'),
        'CACHE_DEFAULT_TIMEOUT': app.config.get('CACHE_TIMEOUT', int(timedelta(hours=6).total_seconds())),
        'CACHE_KEY_PREFIX': app.config.get('CACHE_KEY_PREFIX', 'swahili_culture_'),
        'CACHE_THRESHOLD': app.config.get('CACHE_THRESHOLD', 500),
        'CACHE_REDIS_URL': app.config.get('REDIS_URL', None)
    }
    
    if cache_config['CACHE_TYPE'] == 'redis' and not cache_config['CACHE_REDIS_URL']:
        raise ValueError("Redis cache requires REDIS_URL in configuration")
    
    cache.init_app(app, config=cache_config)
    return cache
