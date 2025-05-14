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
        
        # Structure data for the template
        page_data = {
            "page_title": "Swahili Food",
            "recipe_type": recipe_type,
            "hero": {
                "title": "Swahili Cuisine",
                "subtitle": "The Flavors of East Africa",
                "description": "Discover the unique flavors influenced by African, Arabic, Indian, and coastal traditions. Swahili cuisine features aromatic spices, coconut, seafood, and staple grains prepared with time-honored techniques.",
                "background_image": content.get('hero', {}).get('background_image', url_for('static', filename='img/cultural/food-hero.jpg')),
                "primary_button": {
                    "text": "Explore Recipes",
                    "link": "#recipes"
                },
                "secondary_button": {
                    "text": "Cooking Techniques",
                    "link": "#techniques"
                },
                "breadcrumbs": [
                    {"label": "Cultural Aspects", "link": "/culture"},
                    {"label": "Swahili Food", "link": None}
                ]
            },
            "introduction": {
                "title": "A Culinary Fusion of Cultures",
                "description": "Traditional dishes shaped by centuries of trade and cultural exchange",
                "content_paragraphs": [
                    "Swahili cuisine represents a fascinating culinary fusion that has evolved through centuries of cultural exchange along the East African coast. Drawing influences from indigenous African cooking techniques, Arabic spice traditions, Indian flavor profiles, and Portuguese ingredients, Swahili food stands as a testament to the region's rich trading history.",
                    "Central to Swahili cooking is the skilled use of spices. Complex blends featuring cardamom, cinnamon, cloves, cumin, and black pepper—many of which were historically traded through Swahili ports—create distinctive flavor profiles unique to this cuisine.",
                    "Seafood naturally plays a central role in coastal Swahili cuisine, with preparations highlighting fresh catches prepared with traditional techniques including grilling, frying, or slow-cooking in flavorful sauces, often featuring coconut milk as a key ingredient."
                ]
            },
            "categories": content.get('categories', [
                {"id": "main", "name": "Main Dishes"},
                {"id": "seafood", "name": "Seafood"},
                {"id": "rice", "name": "Rice Dishes"},
                {"id": "stews", "name": "Stews & Curries"},
                {"id": "street", "name": "Street Food"},
                {"id": "bread", "name": "Breads"},
                {"id": "dessert", "name": "Desserts"}
            ]),
            "featured_recipes": content.get('featured', [
                {
                    "title": "Pilau ya Nyama",
                    "short_description": "Aromatic spiced rice with tender meat and a blend of traditional spices - the cornerstone of Swahili celebrations.",
                    "category": "Rice Dishes",
                    "is_vegetarian": False,
                    "difficulty": "Intermediate",
                    "prep_time": "1 hour 30 min",
                    "servings": 6,
                    "image": url_for('static', filename='img/recipes/pilau.jpg'),
                    "link": "/recipes/pilau-ya-nyama"
                },
                {
                    "title": "Samaki wa Kupaka",
                    "short_description": "Grilled fish coated in a rich coconut sauce spiced with garlic, ginger, and tamarind - a coastal specialty.",
                    "category": "Seafood",
                    "is_vegetarian": False,
                    "difficulty": "Intermediate",
                    "prep_time": "45 min",
                    "servings": 4,
                    "image": url_for('static', filename='img/recipes/samaki-kupaka.jpg'),
                    "link": "/recipes/samaki-wa-kupaka"
                },
                {
                    "title": "Mandazi",
                    "short_description": "Lightly sweetened fried bread with a hint of cardamom, perfect as a breakfast treat or afternoon snack.",
                    "category": "Breads",
                    "is_vegetarian": True,
                    "difficulty": "Easy",
                    "prep_time": "40 min",
                    "servings": 12,
                    "image": url_for('static', filename='img/recipes/mandazi.jpg'),
                    "link": "/recipes/mandazi"
                }
            ]),
            "events": content.get('events', [
                {
                    "title": "Swahili Cuisine Showcase",
                    "category": "Food",
                    "color": "#006400",
                    "date": "September 15-16, 2025",
                    "location": "Mombasa, Kenya",
                    "description": "A culinary journey featuring cooking demonstrations, tasting events, and discussions on the cultural significance of Swahili food traditions.",
                    "link": "/events/swahili-cuisine-showcase",
                    "calendar_link": "#add-to-calendar-1"
                },
                {
                    "title": "Coastal Seafood Festival",
                    "category": "Food",
                    "color": "#006400",
                    "date": "October 5, 2025",
                    "location": "Zanzibar, Tanzania",
                    "description": "Celebrating the rich seafood traditions of Zanzibar with chef demonstrations and tastings of classic dishes.",
                    "link": "/events/coastal-seafood-festival",
                    "calendar_link": "#add-to-calendar-2"
                }
            ]),
            "resources": content.get('resources', [
                {
                    "title": "Swahili Cuisine Cookbook",
                    "type": "Print/Digital",
                    "description": "A comprehensive guide to traditional and contemporary Swahili recipes with cultural context and cooking techniques.",
                    "icon": "book",
                    "color": "#006400",
                    "link": "/resources/swahili-cookbook"
                },
                {
                    "title": "Spices of the Swahili Coast",
                    "type": "Guide",
                    "description": "Detailed exploration of essential spices in Swahili cooking, their history, and how to use them effectively.",
                    "icon": "flame",
                    "color": "#006400",
                    "link": "/resources/swahili-spices"
                },
                {
                    "title": "Traditional Cooking Methods",
                    "type": "Video Series",
                    "description": "Step-by-step demonstrations of authentic cooking techniques from clay pot cooking to charcoal grilling.",
                    "icon": "video",
                    "color": "#006400",
                    "link": "/resources/cooking-methods"
                }
            ])
        }
        
        return render_template('cultural/swahili_food.html', **page_data)
    except Exception as e:
        current_app.logger.error(f"Swahili Food page error: {str(e)}")
        return render_template('cultural/swahili_food.html', error=True)

@cultural_bp.route('/fashion')
@cache.cached(timeout=CULTURAL_CACHE_TIMEOUT)
def fashion():
    """Traditional clothing and fashion page"""
    try:
        content = cms.get_content('fashion')
        
        # Structure data for the template
        page_data = {
            "page_title": "Swahili Fashion",
            "hero": {
                "title": "Swahili Fashion",
                "subtitle": "Traditional and Contemporary Textiles",
                "description": "Explore the colorful textiles and designs that represent Swahili identity. From vibrant kanga and kitenge fabrics to intricate hand-embroidered kofia hats, Swahili fashion blends practicality with artistic expression.",
                "background_image": content.get('hero', {}).get('background_image', url_for('static', filename='img/cultural/fashion-hero.jpg')),
                "primary_button": {
                    "text": "Explore Traditional Styles",
                    "link": "#traditional"
                },
                "secondary_button": {
                    "text": "Contemporary Designers",
                    "link": "#designers"
                },
                "breadcrumbs": [
                    {"label": "Cultural Aspects", "link": "/culture"},
                    {"label": "Fashion", "link": None}
                ]
            },
            "introduction": {
                "title": "Textile Traditions of East Africa",
                "description": "A vibrant aspect of cultural expression along the Swahili coast",
                "content_paragraphs": [
                    "Swahili fashion represents a vibrant aspect of cultural expression along the East African coast, characterized by colorful textiles, meaningful designs, and a blend of practical function with artistic beauty.",
                    "The distinctive clothing traditions of Swahili culture reflect the region's historical position as a crossroads of African, Arabic, Indian, and European influences, creating unique styles that continue to evolve today.",
                    "From traditional garments with centuries of history to contemporary adaptations by modern designers, Swahili textiles and fashion elements provide insights into cultural values, social communication, and artistic expression."
                ]
            },
            "traditional_wear": content.get('traditional', []),
            "modern_adaptations": content.get('modern', [
                {
                    "title": "Kanga-Inspired Contemporary Fashion",
                    "category": "Textile Innovation",
                    "description": "<p>Modern designers increasingly incorporate traditional kanga patterns and proverbs into contemporary clothing styles that appeal to global markets while honoring cultural heritage. These adaptations transform the rectangular cloth into structured garments with tailored silhouettes.</p><p>Some designers maintain the traditional messaging aspect of kanga by incorporating authentic proverbs or creating new sayings that resonate with contemporary issues and concerns, allowing the garments to maintain their cultural significance while adopting new forms.</p>",
                    "image": url_for('static', filename='img/fashion/modern-kanga.jpg'),
                    "tags": ["Contemporary", "Kanga-inspired", "Global Market"],
                    "link": "/fashion/modern-kanga",
                    "link_text": "View Collections"
                },
                {
                    "title": "Urban Streetwear with Swahili Elements",
                    "category": "Youth Fashion",
                    "description": "<p>Urban youth in East African cities have developed distinctive streetwear styles that incorporate elements of Swahili textile traditions into contemporary casual fashion. T-shirts featuring kanga proverbs, kitenge-patterned sneakers, and accessories with traditional embroidery patterns represent this cultural fusion.</p><p>These adaptations help younger generations connect with cultural heritage in ways that feel relevant to their daily lives and aesthetic preferences, creating a dynamic conversation between tradition and innovation.</p>",
                    "image": url_for('static', filename='img/fashion/urban-fashion.jpg'),
                    "tags": ["Urban", "Youth", "Streetwear"],
                    "link": "/fashion/urban-swahili",
                    "link_text": "Explore Urban Style"
                },
                {
                    "title": "Formal Wear with Traditional Touches",
                    "category": "Occasion Wear",
                    "description": "<p>Contemporary designers create formal wear that incorporates Swahili design elements for special occasions, including weddings, diplomatic events, and cultural celebrations. These garments often feature hand-embroidery techniques traditionally used on kofia hats applied to modern suit jackets or formal dresses.</p><p>This fusion approach allows individuals to honor cultural traditions while participating in contexts that might call for more internationally recognized formal attire, creating a distinctive sartorial statement that communicates cultural pride.</p>",
                    "image": url_for('static', filename='img/fashion/formal-fusion.jpg'),
                    "tags": ["Formal", "Occasion", "Embroidery"],
                    "link": "/fashion/formal-traditional",
                    "link_text": "View Formal Collections"
                }
            ]),
            "designers": content.get('designers', [
                {
                    "name": "Farida Mohamed",
                    "location": "Mombasa, Kenya",
                    "image": url_for('static', filename='img/designers/farida-mohamed.jpg'),
                    "bio": "Pioneer in contemporary kanga design who combines traditional sayings with modern silhouettes, creating pieces that bridge generations.",
                    "styles": ["Kanga Innovation", "Women's Wear", "Sustainable"],
                    "link": "/designers/farida-mohamed",
                    "instagram": "https://instagram.com/faridadesigns",
                    "website": "https://faridadesigns.com"
                },
                {
                    "name": "Ibrahim Khalil",
                    "location": "Zanzibar, Tanzania",
                    "image": url_for('static', filename='img/designers/ibrahim-khalil.jpg'),
                    "bio": "Specializes in modernizing traditional menswear, especially elaborately embroidered pieces inspired by historical kofia patterns.",
                    "styles": ["Menswear", "Embroidery", "Formal"],
                    "link": "/designers/ibrahim-khalil",
                    "instagram": "https://instagram.com/ibrahimkhalildesigns",
                    "website": "https://khalildesigns.com"
                },
                {
                    "name": "Amina Hassan",
                    "location": "Dar es Salaam, Tanzania",
                    "image": url_for('static', filename='img/designers/amina-hassan.jpg'),
                    "bio": "Award-winning kitenge designer whose bold patterns and innovative cuts have been featured in international fashion magazines.",
                    "styles": ["Kitenge", "Contemporary", "Global"],
                    "link": "/designers/amina-hassan",
                    "instagram": "https://instagram.com/aminahassan",
                    "website": "https://aminahassan.com"
                },
                {
                    "name": "Omar Farid",
                    "location": "Lamu, Kenya",
                    "image": url_for('static', filename='img/designers/omar-farid.jpg'),
                    "bio": "Sustainable fashion advocate who works with traditional artisans to create contemporary pieces using ancient textile techniques.",
                    "styles": ["Sustainable", "Artisanal", "Fusion"],
                    "link": "/designers/omar-farid",
                    "instagram": "https://instagram.com/omarfaridstudio",
                    "website": "https://omarfarid.co.ke"
                },
                {
                    "name": "Zeina Mohammed",
                    "location": "Mombasa, Kenya",
                    "image": url_for('static', filename='img/designers/zeina-mohammed.jpg'),
                    "bio": "Specializes in contemporary modest fashion that incorporates traditional Swahili textile elements with global modest wear trends.",
                    "styles": ["Modest Fashion", "Contemporary", "Global"],
                    "link": "/designers/zeina-mohammed",
                    "instagram": "https://instagram.com/zeinadesigns",
                    "website": "https://zeinadesigns.com"
                },
                {
                    "name": "Abdul Rahman",
                    "location": "Stone Town, Zanzibar",
                    "image": url_for('static', filename='img/designers/abdul-rahman.jpg'),
                    "bio": "Textile innovator who develops new printing techniques for traditional patterns, creating unique contemporary expressions of Swahili aesthetics.",
                    "styles": ["Textile Innovation", "Color Exploration", "Artisanal"],
                    "link": "/designers/abdul-rahman",
                    "instagram": "https://instagram.com/abdulrahmanstudio",
                    "website": "https://abdulrahman.studio"
                }
            ]),
            "events": content.get('events', [
                {
                    "title": "Kanga & Kitenge Exhibition",
                    "category": "Fashion",
                    "color": "#FF7043",
                    "date": "October 10-15, 2025",
                    "location": "Dar es Salaam, Tanzania",
                    "description": "Showcasing traditional textiles and contemporary designs that blend Swahili fashion elements with modern styles.",
                    "link": "/events/kanga-kitenge-exhibition",
                    "calendar_link": "#add-to-calendar-1"
                },
                {
                    "title": "East African Fashion Week",
                    "category": "Fashion",
                    "color": "#FF7043",
                    "date": "November 5-10, 2025",
                    "location": "Nairobi, Kenya",
                    "description": "Runway shows featuring leading Swahili fashion designers alongside other East African creatives, showcasing the region's diverse textile traditions.",
                    "link": "/events/east-african-fashion-week",
                    "calendar_link": "#add-to-calendar-2"
                }
            ]),
            "resources": content.get('resources', [
                {
                    "title": "Kanga Messages & Meanings",
                    "type": "Digital Guide",
                    "description": "A comprehensive collection of traditional kanga sayings with their cultural contexts and interpretations.",
                    "icon": "message-circle",
                    "color": "#FF7043",
                    "link": "/resources/kanga-messages"
                },
                {
                    "title": "Traditional Embroidery Techniques",
                    "type": "Video Series",
                    "description": "Step-by-step demonstrations of the intricate stitching patterns used in kofia hats and other traditional garments.",
                    "icon": "scissors",
                    "color": "#FF7043",
                    "link": "/resources/embroidery-techniques"
                },
                {
                    "title": "Evolution of Swahili Fashion",
                    "type": "eBook",
                    "description": "Historical analysis of how Swahili textiles and garments have changed over time while maintaining cultural connections.",
                    "icon": "book",
                    "color": "#FF7043",
                    "link": "/resources/swahili-fashion-evolution"
                }
            ])
        }
        
        return render_template('cultural/fashion.html', **page_data)
    except Exception as e:
        current_app.logger.error(f"Fashion page error: {str(e)}")
        return render_template('cultural/fashion.html', error=True)

@cultural_bp.route('/heritage')
@cache.cached(timeout=86400)  # 24-hour cache for less changing content
def heritage():
    """Cultural heritage and historical sites page"""
    try:
        region_filter = request.args.get('region', 'all')
        content = cms.get_content(f'heritage?region={region_filter}')
        
        # Structure data for the template
        page_data = {
            "page_title": "Swahili Heritage",
            "current_region": region_filter,
            "hero": {
                "title": "Swahili Heritage",
                "subtitle": "Preserving East Africa's Coastal Legacy",
                "description": "Discover the rich historical legacy of Swahili civilization that developed along the East African coast through centuries of trade, cultural exchange, and urban development.",
                "background_image": content.get('hero', {}).get('background_image', url_for('static', filename='img/cultural/heritage-hero.jpg')),
                "primary_button": {
                    "text": "Explore Historic Sites",
                    "link": "#sites"
                },
                "secondary_button": {
                    "text": "Preservation Efforts",
                    "link": "#preservation"
                },
                "breadcrumbs": [
                    {"label": "Cultural Aspects", "link": "/culture"},
                    {"label": "Heritage", "link": None}
                ]
            },
            "introduction": {
                "title": "A Rich Cultural Legacy",
                "description": "Centuries of maritime trade and cultural exchange along the East African coast",
                "content_paragraphs": [
                    "Swahili heritage encompasses a rich tapestry of historical, architectural, and cultural elements that have evolved along the East African coast over more than a millennium. This heritage reflects the unique position of Swahili civilization as a mediator between African, Middle Eastern, and Asian cultural spheres.",
                    "The architectural heritage of Swahili coastal settlements represents one of the most visible aspects of this legacy. Stone Town in Zanzibar stands as a UNESCO World Heritage site exemplifying the characteristic urban planning and building techniques of Swahili culture.",
                    "Maritime trade lies at the heart of Swahili heritage, with coastal communities having participated in Indian Ocean commercial networks since at least the 8th century. This trade not only brought material goods but facilitated cultural exchange, religious ideas, and technological innovations."
                ]
            },
            "regions": content.get('regions', [
                {"id": "zanzibar", "name": "Zanzibar"},
                {"id": "kenya", "name": "Kenyan Coast"},
                {"id": "tanzania", "name": "Tanzanian Coast"},
                {"id": "mozambique", "name": "Northern Mozambique"},
                {"id": "comoros", "name": "Comoros Islands"}
            ]),
            "sites": content.get('sites', [
                {
                    "name": "Stone Town",
                    "location": "Zanzibar, Tanzania",
                    "description": "The historic center of Zanzibar City features a unique mixture of Arab, Persian, Indian, and European elements with distinctly Swahili architectural style. Notable for its carved doors, narrow streets, and coral stone buildings.",
                    "image": url_for('static', filename='img/heritage/stone-town.jpg'),
                    "unesco": True,
                    "featured": True,
                    "tags": ["Architecture", "UNESCO", "Urban Center"],
                    "link": "/heritage/stone-town",
                    "map_link": "https://goo.gl/maps/stonetwon"
                },
                {
                    "name": "Lamu Old Town",
                    "location": "Lamu Island, Kenya",
                    "description": "The oldest and best-preserved Swahili settlement in East Africa, featuring traditional Swahili architecture with inner courtyards, verandas, and elaborately carved wooden doors. A living cultural heritage site where traditional lifestyles continue.",
                    "image": url_for('static', filename='img/heritage/lamu.jpg'),
                    "unesco": True,
                    "featured": True,
                    "tags": ["Architecture", "UNESCO", "Living Heritage"],
                    "link": "/heritage/lamu",
                    "map_link": "https://goo.gl/maps/lamu"
                },
                {
                    "name": "Kilwa Kisiwani",
                    "location": "Southern Tanzania",
                    "description": "Ruins of a medieval sultanate that was once East Africa's most powerful trading center, controlling gold trade from present-day Zimbabwe. Features impressive palace structures, a Great Mosque, and extensive fortifications.",
                    "image": url_for('static', filename='img/heritage/kilwa.jpg'),
                    "unesco": True,
                    "featured": True,
                    "tags": ["Archaeological", "UNESCO", "Medieval"],
                    "link": "/heritage/kilwa",
                    "map_link": "https://goo.gl/maps/kilwa"
                },
                {
                    "name": "Bagamoyo",
                    "location": "Tanzanian Coast",
                    "description": "Former capital of German East Africa and major terminus of slave and ivory caravans from the interior. Historic buildings reflect Swahili, Arab, German colonial, and Indian architectural influences.",
                    "image": url_for('static', filename='img/heritage/bagamoyo.jpg'),
                    "unesco": False,
                    "featured": True,
                    "tags": ["Colonial", "Slave Trade History", "Port"],
                    "link": "/heritage/bagamoyo",
                    "map_link": "https://goo.gl/maps/bagamoyo"
                },
                {
                    "name": "Mombasa Old Town",
                    "location": "Mombasa, Kenya",
                    "description": "Historic district featuring narrow streets, carved balconies, and distinctive Swahili doors. The area includes Fort Jesus, a 16th-century Portuguese fortress that demonstrates the strategic importance of Mombasa in colonial history.",
                    "image": url_for('static', filename='img/heritage/mombasa.jpg'),
                    "unesco": False,
                    "featured": True,
                    "tags": ["Urban", "Colonial", "Mixed Heritage"],
                    "link": "/heritage/mombasa",
                    "map_link": "https://goo.gl/maps/mombasa"
                },
                {
                    "name": "Ilha de Moçambique",
                    "location": "Nampula Province, Mozambique",
                    "description": "Small island that served as the Portuguese colonial capital for nearly four centuries. Features stone and lime town with Swahili, Arab, and European architectural elements reflecting its complex history.",
                    "image": url_for('static', filename='img/heritage/mozambique-island.jpg'),
                    "unesco": True,
                    "featured": True,
                    "tags": ["Colonial", "UNESCO", "Island"],
                    "link": "/heritage/mozambique-island",
                    "map_link": "https://goo.gl/maps/mozambique"
                }
            ]),
            "events": content.get('events', [
                {
                    "title": "Swahili Cultural Heritage Symposium",
                    "category": "Heritage",
                    "color": "#D4AF37",
                    "date": "November 10-12, 2025",
                    "location": "Zanzibar, Tanzania",
                    "description": "Academic and community discussions on preserving and promoting Swahili cultural heritage in the modern world, featuring presentations by leading experts and community representatives.",
                    "link": "/events/swahili-heritage-symposium",
                    "calendar_link": "#add-to-calendar-1"
                },
                {
                    "title": "Lamu Cultural Festival",
                    "category": "Heritage",
                    "color": "#D4AF37",
                    "date": "December 5-8, 2025",
                    "location": "Lamu, Kenya",
                    "description": "Annual celebration of Swahili culture featuring traditional music, dance, dhow races, donkey races, and culinary showcases in the historic UNESCO World Heritage site.",
                    "link": "/events/lamu-festival-2025",
                    "calendar_link": "#add-to-calendar-2"
                }
            ]),
            "resources": content.get('resources', [
                {
                    "title": "Stone Town Architecture Guide",
                    "type": "Digital Tour",
                    "description": "Interactive exploration of architectural features in Zanzibar's historic district with detailed explanations of historical influences and construction techniques.",
                    "icon": "building",
                    "color": "#D4AF37",
                    "link": "/resources/stone-town-architecture"
                },
                {
                    "title": "Swahili Oral Traditions Archive",
                    "type": "Audio Collection",
                    "description": "Recorded narratives, songs, and poetic performances preserving the intangible heritage of Swahili communities along the East African coast.",
                    "icon": "mic",
                    "color": "#D4AF37",
                    "link": "/resources/oral-traditions-archive"
                },
                {
                    "title": "Maritime Trade Routes",
                    "type": "Interactive Map",
                    "description": "Visualization of historical Indian Ocean trade networks that connected Swahili city-states to ports across Asia, the Middle East, and the African interior.",
                    "icon": "ship",
                    "color": "#D4AF37",
                    "link": "/resources/trade-routes-map"
                }
            ])
        }
        
        return render_template('cultural/heritage.html', **page_data)
    except Exception as e:
        current_app.logger.error(f"Heritage page error: {str(e)}")
        return render_template('cultural/heritage.html', error=True)
    