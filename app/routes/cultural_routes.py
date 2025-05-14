#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/routes/cultural_routes.py


from flask import Blueprint, render_template, current_app, request, url_for
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
        # Get content from CMS
        content = cms.get_content('swahili-language')
        
        # Structure the data for the template
        page_data = {
            "page_title": "Swahili Language",
            "hero": {
                "title": "Swahili Language",
                "subtitle": "Explore the Rich Linguistic Heritage",
                "description": "Discover the rich heritage of Kiswahili, spoken by over 230 million people worldwide, originating from the Bantu languages of East Africa and evolving through centuries of trade and cultural exchange.",
                "background_image": content.get('hero', {}).get('background_image', url_for('static', filename='img/cultural/swahili-language-hero.jpg')),
                "primary_button": {
                    "text": "Start Learning",
                    "link": "#lessons"
                },
                "secondary_button": {
                    "text": "Explore Resources",
                    "link": "#resources"
                },
                "breadcrumbs": [
                    {"label": "Cultural Aspects", "link": "/culture"},
                    {"label": "Swahili Language", "link": None}
                ]
            },
            "introduction": {
                "title": "The Foundation of Swahili Culture",
                "description": "A language that connects nations across Eastern and Central Africa",
                "content_paragraphs": [
                    "Kiswahili originated from the Bantu languages spoken by the indigenous people of the East African coast. The language developed as a result of trade and cultural exchange between the local population and foreign traders, sailors, and settlers.",
                    "In the 8th century, Arabic traders and Islamic scholars arrived on the East African coast, bringing their language, culture, and religion. Swahili borrowed heavily from Arabic, incorporating many loanwords, especially in fields like trade, navigation, and Islam.",
                    "Today, Kiswahili is one of the most widely used languages of the African family, and the most widely spoken in Sub-Saharan Africa. It is among the 10 most widely spoken languages in the world, with more than 230 million speakers."
                ]
            },
            "details": {
                "overview": {
                    "content": """
                        <p>Kiswahili is a Bantu language that serves as the lingua franca of East Africa and beyond. As one of Africa's most influential languages, it facilitates communication across diverse ethnic groups and national boundaries.</p>
                        <p>The language features a logical grammatical structure organized around noun classes, with prefixes and affixes modifying words to indicate tense, pluralization, and other attributes. This systematic structure makes Swahili relatively accessible to learners despite its initial unfamiliarity to speakers of European languages.</p>
                        <p>Swahili's vocabulary reflects its rich history of cultural exchange, with approximately 30-40% of words deriving from Arabic, alongside Persian, Portuguese, German, and English influences. This lexical diversity creates a linguistic tapestry that tells the story of East Africa's historical connections.</p>
                    """,
                    "image": url_for('static', filename='img/cultural/swahili-books.jpg'),
                    "image_caption": "Traditional Swahili literature and modern learning materials",
                    "features": [
                        "Official language in Kenya, Tanzania, Uganda, and the Democratic Republic of Congo",
                        "Recognized working language of the African Union and East African Community",
                        "UNESCO World Kiswahili Language Day celebrated annually on July 7th",
                        "Growing global interest with programs at major universities worldwide"
                    ]
                },
                "history": {
                    "content": """
                        <p>Swahili's origins trace back to coastal Bantu languages that evolved through contact with Arab, Persian, and other traders along the Indian Ocean trade routes. The earliest Swahili documents date to the early 18th century, written in Arabic script, though the oral tradition extends much further back.</p>
                        <p>During the colonial period, European powers standardized written Swahili using the Latin alphabet. German linguists in Tanganyika and British administrators in Kenya played significant roles in codifying grammar and vocabulary, often based on the Zanzibar dialect (Kiunguja).</p>
                        <p>Post-independence African nations embraced Swahili as a unifying, non-tribal language that could help forge national identities beyond colonial linguistic legacies. Tanzania particularly promoted Swahili as the primary national language used in education, government, and daily life.</p>
                    """,
                    "image": url_for('static', filename='img/cultural/swahili-manuscript.jpg'),
                    "image_caption": "Historical Swahili manuscript in Arabic script",
                    "timeline": [
                        {
                            "date": "8th Century",
                            "title": "Early Development",
                            "description": "Formation of early Swahili dialects along the East African coast through interaction between Bantu speakers and Arab traders."
                        },
                        {
                            "date": "13th-15th Century",
                            "title": "Golden Age of Swahili City-States",
                            "description": "Flourishing of Swahili culture and language in city-states like Kilwa, Mombasa, and Zanzibar."
                        },
                        {
                            "date": "19th Century",
                            "title": "Standardization Begins",
                            "description": "European missionaries and colonial administrators begin documenting and standardizing Swahili."
                        },
                        {
                            "date": "1930",
                            "title": "Official Standardization",
                            "description": "The Inter-territorial Language Committee standardizes Swahili based on the Zanzibar dialect."
                        },
                        {
                            "date": "1960s-70s",
                            "title": "Post-Independence Promotion",
                            "description": "Newly independent East African nations adopt Swahili as an official language to promote unity."
                        },
                        {
                            "date": "2021",
                            "title": "UNESCO Recognition",
                            "description": "UNESCO designates July 7th as World Kiswahili Language Day, the first for an African language."
                        }
                    ]
                }
            },
            "lessons": content.get('lessons', [
                {
                    "title": "Greetings and Introductions",
                    "description": "Learn essential Swahili greetings and how to introduce yourself",
                    "thumbnail": url_for('static', filename='img/lessons/greetings.jpg'),
                    "level": "Beginner",
                    "duration": "15 minutes",
                    "video_url": "#video-lesson-1",
                    "url": "/lessons/swahili/greetings"
                },
                {
                    "title": "Everyday Vocabulary",
                    "description": "Common words and phrases for daily communication",
                    "thumbnail": url_for('static', filename='img/lessons/vocabulary.jpg'),
                    "level": "Beginner",
                    "duration": "20 minutes",
                    "video_url": "#video-lesson-2",
                    "url": "/lessons/swahili/vocabulary"
                },
                {
                    "title": "Noun Classes",
                    "description": "Understanding the foundation of Swahili grammar",
                    "thumbnail": url_for('static', filename='img/lessons/grammar.jpg'),
                    "level": "Intermediate",
                    "duration": "30 minutes",
                    "video_url": "#video-lesson-3",
                    "url": "/lessons/swahili/noun-classes"
                }
            ]),
            "events": content.get('events', [
                {
                    "title": "World Kiswahili Language Day",
                    "category": "Language",
                    "color": "#003366",
                    "date": "July 7, 2025",
                    "location": "Virtual & In-Person",
                    "description": "Join us for a celebration of Swahili language and culture featuring speakers, performances, and interactive workshops.",
                    "link": "/events/world-kiswahili-day-2025",
                    "calendar_link": "#add-to-calendar-1"
                },
                {
                    "title": "Swahili Poetry Evening",
                    "category": "Literature",
                    "color": "#D4AF37",
                    "date": "August 12, 2025",
                    "location": "Nairobi, Kenya",
                    "description": "Experience the beauty of traditional and contemporary Swahili poetry through readings and performances.",
                    "link": "/events/swahili-poetry-evening",
                    "calendar_link": "#add-to-calendar-2"
                }
            ]),
            "resources": content.get('resources', [
                {
                    "title": "Comprehensive Swahili Dictionary",
                    "type": "Reference",
                    "description": "An extensive Swahili-English dictionary with over 50,000 entries including modern terminology.",
                    "icon": "book",
                    "color": "#003366",
                    "link": "/resources/swahili-dictionary"
                },
                {
                    "title": "Swahili Grammar Guide",
                    "type": "Learning",
                    "description": "A detailed guide to Swahili grammar with examples and practice exercises.",
                    "icon": "file-text",
                    "color": "#2D8C9E",
                    "link": "/resources/swahili-grammar-guide"
                },
                {
                    "title": "Swahili Conversation Podcast",
                    "type": "Audio",
                    "description": "Weekly podcasts featuring natural conversations in Swahili with transcripts and translations.",
                    "icon": "headphones",
                    "color": "#D4AF37",
                    "link": "/resources/swahili-podcast"
                }
            ])
        }
        
        return render_template('cultural/swahili_language.html', **page_data)
    except Exception as e:
        current_app.logger.error(f"Swahili Language page error: {str(e)}")
        return render_template('cultural/swahili_language.html', error=True)

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