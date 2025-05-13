#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# File: py_swahili_afro/app/services/cms_client.py

from flask import current_app
from app.utils.cache import cache
import requests
import os

class CMSClient:
    @cache.memoize(timeout=3600)  # Cache for 1 hour
    def get_content(self, content_type):
        try:
            response = requests.get(
                f"{os.getenv('CMS_BASE_URL')}/{content_type}",
                headers={'Authorization': f'Bearer {os.getenv('CMS_API_KEY')}'}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            current_app.logger.error(f"CMS API Error: {str(e)}")
            return None
        