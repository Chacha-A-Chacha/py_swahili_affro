#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: py_swahili_afro/app/routes/main_routes.py

from flask import Blueprint, render_template, current_app, request, url_for, redirect, flash
from app.services.cms_client import CMSClient
from app.utils.cache import cache

main_bp = Blueprint('main', __name__, template_folder='templates/main')

cms = CMSClient()

@main_bp.route('/')
@cache.cached(timeout=300)  # Cache homepage for 5 minutes
def home():
    """Home page with dynamic content from CMS"""

    # Hero section content
    hero_content = {
        "badge": "Est. 2024",
        "headline": "Connecting Cultures, Celebrating Swahili Heritage",
        "subheadline": "Swahili Afro Jamboree brings together Swahili and non-Swahili speakers globally for cultural exchange, celebration, and learning.",
        "primary_button": {
            "text": "Explore Events",
            "url": "/events"
        },
        "secondary_button": {
            "text": "Learn More",
            "url": "/about"
        },
        "main_image": "/static/img/kinu.jpg",
        "image_alt": "Swahili cultural celebration",
        "overlay_title": "Experience Swahili Culture",
        "overlay_subtitle": "Music, art, dance, language and cuisine",
        "featured_event": {
            "date": "July 7, 2025",
            "title": "World Kiswahili Language Day",
            "description": "Global celebration of the first African language recognized by the UN",
            "url": "/events/world-kiswahili-day",
            "button_text": "Register Now"
        }
    }

    # Featured content sections
    featured = {
        "events_section": {
            "tag": "Join Us",
            "title": "Upcoming Events",
            "description": "Experience the richness of Swahili culture through our carefully curated events spanning multiple continents.",
            "button_text": "View All Events",
            "button_url": "/events"
        },
        "events": [
            {
                "id": 1,
                "title": "World Kiswahili Language Day",
                "date": "July 7, 2025",
                "time": "10:00 AM - 6:00 PM",
                "location": "Global Event (Online & In-Person)",
                "description": "Join us for the global celebration of the first African language recognized by the UN. Experience panels, performances, and cultural showcases.",
                "image": "/static/img/events/kiswahili-day.jpg",
                "tag": "Featured",
                "url": "/events/1"
            },
            {
                "id": 2,
                "title": "EAKC Swahili Conference",
                "date": "July 5-7, 2025",
                "time": "9:00 AM - 5:00 PM",
                "location": "Dar es Salaam, Tanzania",
                "description": "Three days of academic and cultural exchange focused on the Swahili language and its global impact.",
                "image": "/static/img/events/conference.jpg",
                "tag": "Conference",
                "url": "/events/2"
            },
            {
                "id": 3,
                "title": "Swahili Jamboree Gathering",
                "date": "August 2025",
                "time": "All Day Event",
                "location": "Maryland, USA",
                "description": "Experience the vibrant celebration of Swahili culture through food, music, dance, and more.",
                "image": "/static/img/events/gathering.jpg",
                "tag": "Festival",
                "url": "/events/3"
            },
            {
                "id": 4,
                "title": "Swahili Jamboree Annual Event",
                "date": "July 2026",
                "time": "All Day Event",
                "location": "Maryland, USA",
                "description": "Our flagship annual event bringing together Swahili enthusiasts from around the world.",
                "image": "/static/img/events/annual.jpg",
                "tag": "Annual",
                "url": "/events/4"
            }
        ]
    }

    try:
        content = cms.get_content('home')
        return render_template('main/home.html', 
                           hero_content=hero_content,
                           featured=featured)
                           
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

# routes/main_routes.py

@main_bp.route('/events')
@cache.cached(timeout=180)  # Cache events for 3 minutes
def events():
    """Events listing page with upcoming and past events"""
    try:
        # Sample event data that would normally come from a database or CMS
        upcoming_events = [
            {
                "id": 1,
                "title": "World Kiswahili Language Day",
                "date": "July 7, 2025",
                "time": "10:00 AM - 6:00 PM",
                "location": "Global Event (Online & In-Person)",
                "description": "Join us for the global celebration of the first African language recognized by the UN. Experience panels, performances, and cultural showcases.",
                "image": url_for('static', filename='img/events/kiswahili-day.jpg'),
                "tag": "Featured",
                "is_hybrid": True,
                "location_detail": "Multiple venues globally with main hub in Dar es Salaam, Tanzania",
                "features": [
                    "Panel discussions with linguistic experts",
                    "Live performances showcasing Swahili arts and literature",
                    "Interactive language workshops for beginners and advanced speakers",
                    "Virtual participation options for global attendees"
                ]
            },
            {
                "id": 2,
                "title": "EAKC Swahili Conference",
                "date": "July 5-7, 2025",
                "time": "9:00 AM - 5:00 PM",
                "location": "Dar es Salaam, Tanzania",
                "description": "Three days of academic and cultural exchange focused on the Swahili language and its global impact.",
                "image": url_for('static', filename='img/events/conference.jpg'),
                "tag": "Conference",
                "is_hybrid": True,
                "location_detail": "Salamanda Towers Conference Center, Dar es Salaam",
                "features": [
                    "Latest research on Swahili linguistics and literature",
                    "Pedagogical innovations in Swahili language education",
                    "Cultural contexts and contemporary applications",
                    "Networking opportunities with Swahili language professionals"
                ]
            },
            {
                "id": 3,
                "title": "Swahili Jamboree Gathering",
                "date": "August 2025",
                "time": "All Day Event",
                "location": "Maryland, USA",
                "description": "Experience the vibrant celebration of Swahili culture through food, music, dance, and more.",
                "image": url_for('static', filename='img/events/gathering.jpg'),
                "tag": "Festival",
                "is_hybrid": False,
                "location_detail": "Alan Linton Community Center, Frederick, Maryland",
                "features": [
                    "Traditional and contemporary Swahili cuisine tastings",
                    "Live music and dance performances",
                    "Artisan marketplace featuring authentic crafts",
                    "Children's activities and cultural education opportunities"
                ]
            },
            {
                "id": 4,
                "title": "Swahili Jamboree Annual Event",
                "date": "July 2026",
                "time": "All Day Event",
                "location": "Maryland, USA",
                "description": "Our flagship annual event bringing together Swahili enthusiasts from around the world.",
                "image": url_for('static', filename='img/events/annual.jpg'),
                "tag": "Annual",
                "is_hybrid": False,
                "location_detail": "To be announced, Maryland USA",
                "features": [
                    "Multiple performance stages with artists from across the Swahili-speaking world",
                    "Culinary festival with renowned chefs",
                    "Fashion showcase of traditional and contemporary Swahili designs",
                    "Business networking and cultural exchange forums"
                ]
            }
        ]
        
        past_events = [
            {
                "id": 101,
                "title": "Swahili Jamboree Inaugural Event",
                "date": "July 2024",
                "location": "Maryland, USA",
                "image": url_for('static', filename='img/events/past-inaugural.jpg'),
                "testimonial": "A wonderful cultural experience that brought Swahili culture to life for everyone present!"
            },
            {
                "id": 102,
                "title": "Swahili Cultural Workshop",
                "date": "March 2024",
                "location": "Online",
                "image": url_for('static', filename='img/events/past-workshop.jpg'),
                "testimonial": "The virtual format made it accessible globally while still maintaining an intimate, engaging atmosphere."
            },
            {
                "id": 103,
                "title": "East African Language Festival",
                "date": "November 2023",
                "location": "Dar es Salaam, Tanzania",
                "image": url_for('static', filename='img/events/past-festival.jpg'),
                "testimonial": "An enriching celebration of East African linguistic diversity with Swahili at its heart."
            }
        ]
        
        faqs = [
            {
                "question": "Do I need to speak Swahili to attend your events?",
                "answer": "Not at all! Our events welcome everyone interested in Swahili culture, regardless of language proficiency. Many activities are designed for non-speakers, and translation services are available at most events."
            },
            {
                "question": "Are there discounts available for students or groups?",
                "answer": "Yes, we offer special rates for students, educators, and groups of 5 or more people. Please contact our events team for details."
            },
            {
                "question": "How can I present or showcase my work at your events?",
                "answer": "We welcome proposals for presentations, performances, and exhibits. Please submit your proposal through our online form at least 3 months before the event date."
            },
            {
                "question": "Are the events family-friendly?",
                "answer": "Most of our events are designed to be enjoyed by all ages, with specific activities for children and youth. Event descriptions will note any age restrictions."
            },
            {
                "question": "Can I volunteer at the events?",
                "answer": "Absolutely! We rely on volunteers to help make our events successful. You can apply to volunteer on our website and select areas you're interested in supporting."
            }
        ]
        
        return render_template('main/events.html', 
                           upcoming_events=upcoming_events,
                           past_events=past_events,
                           faqs=faqs)
    except Exception as e:
        current_app.logger.error(f"Events page error: {str(e)}")
        return render_template('main/events.html', 
                           upcoming_events=[],
                           past_events=[],
                           faqs=[],
                           error=True)

# Individual event detail page
@main_bp.route('/events/<int:event_id>')
def event_detail(event_id):
    """Individual event detail page"""
    try:
        # In a real application, you would fetch the specific event from your database
        # For this example, we'll just return a generic template with the ID
        return render_template('main/event_detail.html', event_id=event_id)
    except Exception as e:
        current_app.logger.error(f"Event detail page error: {str(e)}")
        return render_template('main/error.html', 
                           error_message="Event not found")

# Event registration handler
@main_bp.route('/events/register/<int:event_id>', methods=['GET', 'POST'])
def event_register(event_id):
    """Event registration page and form handler"""
    if request.method == 'POST':
        try:
            # Process registration form
            name = request.form.get('name')
            email = request.form.get('email')
            # Additional form fields...
            
            # In a real app, save this to database and send confirmation email
            
            return redirect(url_for('main.event_register_success', event_id=event_id))
        except Exception as e:
            current_app.logger.error(f"Event registration error: {str(e)}")
            return render_template('main/event_register.html', 
                               event_id=event_id,
                               error="Registration failed. Please try again.")
    
    # GET request - show the registration form
    return render_template('main/event_register.html', event_id=event_id)

# Registration success page
@main_bp.route('/events/register/success/<int:event_id>')
def event_register_success(event_id):
    """Registration success confirmation page"""
    return render_template('main/event_register_success.html', event_id=event_id)

# Past events gallery 
@main_bp.route('/events/gallery/<int:event_id>')
def event_gallery(event_id):
    """Event photo gallery page"""
    # In a real app, fetch photos for this event
    return render_template('main/event_gallery.html', event_id=event_id)

# All past events listing
@main_bp.route('/events/past')
def past_events():
    """Complete listing of past events"""
    # In a real app, fetch all past events, possibly with pagination
    return render_template('main/past_events.html')

# routes/main_routes.py

@main_bp.route('/news')
@cache.cached(timeout=300)  # Cache for 5 minutes
def news():
    """News and articles page with featured content, categories, and media gallery"""
    try:
        # Featured article data
        featured_article = {
            "id": 1,
            "title": "UNESCO Celebrates World Kiswahili Language Day for the First Time",
            "excerpt": "Recognition of Kiswahili as the first African language to have its own UN-recognized international day marks a significant milestone for African languages and culture.",
            "content": """
                <p>July 7th, 2025 will mark an extraordinary celebration as UNESCO observes World Kiswahili Language Day for the first time, following the resolution adopted at its 41st General Conference in 2021. This landmark recognition makes Kiswahili the first African language to have its own UN-designated international day.</p>
                
                <p>Kiswahili, one of the most widely spoken languages in Africa with over 230 million speakers, serves as an official language for the African Union, the East African Community, and several African nations including Tanzania, Kenya, and Uganda.</p>
                
                <p>"This recognition is not just about a language, but about the rich cultural heritage and the vibrant communities that have preserved and evolved Kiswahili over centuries," explains Mr. Paul Mabeba, President of Swahili Afro Jamboree. "It acknowledges the significant role that Kiswahili has played in regional integration, cross-cultural exchange, and the preservation of indigenous knowledge."</p>
                
                <p>The Swahili Afro Jamboree organization is planning a series of events to commemorate this historic occasion, including international conferences, cultural showcases, and educational initiatives across multiple continents.</p>
                
                <p>The designation of World Kiswahili Language Day represents a growing global appreciation for linguistic diversity and the importance of preserving and celebrating languages as vehicles of cultural identity and heritage.</p>
            """,
            "author": "Editorial Team",
            "date": "April 10, 2025",
            "read_time": "4 min read",
            "category": "Cultural Recognition",
            "tags": ["UNESCO", "Kiswahili", "Language", "Cultural Heritage"],
            "image": url_for('static', filename='img/news/featured-unesco.jpg'),
            "likes": 142,
            "comments": 37
        }
        
        # Recent news articles
        recent_news = [
            {
                "id": 2,
                "title": "Swahili Afro Jamboree Partners with Leading Universities for Language Programs",
                "excerpt": "New educational initiatives aim to expand access to Swahili language learning resources globally.",
                "author": "Sarah Johnson",
                "date": "March 28, 2025",
                "read_time": "3 min read",
                "category": "Education",
                "image": url_for('static', filename='img/news/university-partners.jpg')
            },
            {
                "id": 3,
                "title": "Annual Swahili Cultural Festival Announces Expanded Program for 2025",
                "excerpt": "This year's event will feature performers and participants from twelve countries across three continents.",
                "author": "Michael Kamau",
                "date": "March 15, 2025",
                "read_time": "5 min read",
                "category": "Events",
                "image": url_for('static', filename='img/news/cultural-festival.jpg')
            },
            {
                "id": 4,
                "title": "Swahili Cuisine Gains International Recognition in Culinary Competition",
                "excerpt": "Traditional East African dishes receive accolades at international food festival, highlighting the growing global interest in African cuisine.",
                "author": "Amina Hassan",
                "date": "February 22, 2025",
                "read_time": "4 min read",
                "category": "Cuisine",
                "image": url_for('static', filename='img/news/swahili-cuisine.jpg')
            }
        ]
        
        # Article categories
        article_categories = [
            { "name": "All", "count": 24 },
            { "name": "Cultural Heritage", "count": 8 },
            { "name": "Language", "count": 6 },
            { "name": "Events", "count": 5 },
            { "name": "Cuisine", "count": 3 },
            { "name": "Fashion", "count": 2 }
        ]
        
        # Popular tags
        popular_tags = [
            { "name": "Swahili", "count": 18 },
            { "name": "Culture", "count": 15 },
            { "name": "East Africa", "count": 12 },
            { "name": "Language", "count": 10 },
            { "name": "UNESCO", "count": 7 },
            { "name": "Heritage", "count": 6 },
            { "name": "Music", "count": 5 },
            { "name": "Dance", "count": 5 },
            { "name": "Cuisine", "count": 4 },
            { "name": "Fashion", "count": 3 }
        ]
        
        # All articles
        all_articles = [
            {
                "id": 5,
                "title": "The Evolution of Swahili Music: Traditional to Contemporary",
                "excerpt": "Exploring the rich musical journey from traditional taarab to modern afrofusion sounds.",
                "author": "David Ndungu",
                "date": "February 10, 2025",
                "read_time": "6 min read",
                "category": "Cultural Heritage",
                "image": url_for('static', filename='img/news/swahili-music.jpg')
            },
            {
                "id": 6,
                "title": "Kiswahili in the Digital Age: Language Preservation Through Technology",
                "excerpt": "How digital tools and platforms are helping to preserve and promote Swahili language learning.",
                "author": "Leila Mohammed",
                "date": "January 25, 2025",
                "read_time": "5 min read",
                "category": "Language",
                "image": url_for('static', filename='img/news/digital-language.jpg')
            },
            {
                "id": 7,
                "title": "Swahili Fashion Week Highlights Cultural Fusion in Modern Design",
                "excerpt": "Designers showcase innovative creations blending traditional textiles with contemporary styles.",
                "author": "Grace Kimani",
                "date": "January 12, 2025",
                "read_time": "4 min read",
                "category": "Fashion",
                "image": url_for('static', filename='img/news/fashion-week.jpg')
            },
            {
                "id": 8,
                "title": "The Art of Swahili Storytelling: Preserving Oral Traditions",
                "excerpt": "How traditional narratives and proverbs continue to shape contemporary Swahili culture.",
                "author": "Hassan Omar",
                "date": "December 18, 2024",
                "read_time": "7 min read",
                "category": "Cultural Heritage",
                "image": url_for('static', filename='img/news/storytelling.jpg')
            },
            {
                "id": 9,
                "title": "Exploring the Architectural Heritage of Swahili Coastal Towns",
                "excerpt": "The unique blend of Arabic, Indian, and African influences in historic Stone Town buildings.",
                "author": "Fatima Salim",
                "date": "November 30, 2024",
                "read_time": "6 min read",
                "category": "Cultural Heritage",
                "image": url_for('static', filename='img/news/coastal-architecture.jpg')
            },
            {
                "id": 10,
                "title": "Traditional Swahili Spices: A Culinary Journey Through East Africa",
                "excerpt": "Discovering the essential spice blends that give Swahili cuisine its distinctive flavor profile.",
                "author": "Ibrahim Juma",
                "date": "November 15, 2024",
                "read_time": "5 min read",
                "category": "Cuisine",
                "image": url_for('static', filename='img/news/spices.jpg')
            }
        ]
        
        # Press releases
        press_releases = [
            {
                "id": 1,
                "title": "Swahili Afro Jamboree Announces Partnership with UNESCO for World Kiswahili Language Day",
                "date": "April 5, 2025",
                "excerpt": "The organization will collaborate with UNESCO to host international celebrations and educational programs."
            },
            {
                "id": 2,
                "title": "Annual Swahili Cultural Festival Expands to Three Continents",
                "date": "March 20, 2025",
                "excerpt": "The festival will now include events in North America, Europe, and East Africa, connecting Swahili communities globally."
            },
            {
                "id": 3,
                "title": "New Educational Initiative to Promote Swahili Language Learning",
                "date": "February 15, 2025",
                "excerpt": "Partnership with leading universities will create accessible digital resources for Swahili language learning."
            }
        ]
        
        # Media gallery items
        media_items = [
            {
                "id": 1,
                "type": "photo",
                "title": "Swahili Dance Performance at Cultural Festival",
                "thumbnail": url_for('static', filename='img/media/dance-performance.jpg'),
                "date": "March 2025"
            },
            {
                "id": 2,
                "type": "video",
                "title": "Traditional Swahili Music Showcase",
                "thumbnail": url_for('static', filename='img/media/music-showcase.jpg'),
                "date": "February 2025",
                "duration": "5:24"
            },
            {
                "id": 3,
                "type": "photo",
                "title": "Swahili Fashion Exhibition",
                "thumbnail": url_for('static', filename='img/media/fashion-exhibition.jpg'),
                "date": "January 2025"
            },
            {
                "id": 4,
                "type": "audio",
                "title": "Podcast: The Evolution of Swahili Language",
                "thumbnail": url_for('static', filename='img/media/podcast-language.jpg'),
                "date": "December 2024",
                "duration": "32:15"
            }
        ]
        
        # Social media posts
        social_posts = [
            {
                "id": 1,
                "platform": "facebook",
                "content": "Join us on July 7th for the historic celebration of World Kiswahili Language Day! #SwahiliDay #CulturalHeritage",
                "date": "2 days ago",
                "engagement": "256 likes • 45 shares"
            },
            {
                "id": 2,
                "platform": "twitter",
                "content": "Excited to announce our partnership with major universities to expand access to Swahili language learning resources! #SwahiliLanguage #Education",
                "date": "3 days ago",
                "engagement": "189 likes • 67 retweets"
            },
            {
                "id": 3,
                "platform": "instagram",
                "content": "Throwback to last year's amazing Swahili Cultural Festival! We're making this year's event even bigger and better. #SwahiliCulture #Festival",
                "date": "1 week ago",
                "engagement": "423 likes • 32 comments"
            }
        ]
        
        # Social media links
        social_links = {
            "facebook": "https://facebook.com/swahiliafrojamboree",
            "twitter": "https://twitter.com/swahilijamboree",
            "instagram": "https://instagram.com/swahiliafrojamboree",
            "linkedin": "https://linkedin.com/company/swahili-afro-jamboree"
        }
        
        return render_template('main/news.html', 
                          featured_article=featured_article,
                          recent_news=recent_news,
                          article_categories=article_categories,
                          popular_tags=popular_tags,
                          all_articles=all_articles,
                          press_releases=press_releases,
                          media_items=media_items,
                          social_posts=social_posts,
                          social_links=social_links)
    except Exception as e:
        current_app.logger.error(f"News page error: {str(e)}")
        return render_template('main/error.html', 
                           error_message="Failed to load news content")

# Article detail page
@main_bp.route('/news/article/<int:article_id>')
def article_detail(article_id):
    """Individual article detail page"""
    # In a real application, you would fetch the specific article from your database
    try:
        # For this example, we'll return a simple placeholder
        return render_template('main/article_detail.html', article_id=article_id)
    except Exception as e:
        current_app.logger.error(f"Article detail error: {str(e)}")
        return render_template('main/error.html', error_message="Article not found")

# Newsletter subscription handler
@main_bp.route('/subscribe', methods=['POST'])
def subscribe():
    """Handle newsletter subscription"""
    try:
        email = request.form.get('email')
        # In a real app, save this to database and send confirmation email
        
        # Redirect back to referring page or homepage with success message
        flash("Thank you for subscribing to our newsletter!", "success")
        return redirect(request.referrer or url_for('main.home'))
    except Exception as e:
        current_app.logger.error(f"Subscription error: {str(e)}")
        flash("There was a problem with your subscription. Please try again.", "error")
        return redirect(request.referrer or url_for('main.home'))

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