import requests
from bs4 import BeautifulSoup
import mysql.connector
import re

# List of websites
websites = [
    "https://www.google.com",
    "https://www.bing.com",
    "https://www.yahoo.com",
    "https://www.duckduckgo.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.linkedin.com",
    "https://www.instagram.com",
    "https://www.reddit.com",
    "https://www.pinterest.com",
    "https://www.snapchat.com",
    "https://www.tumblr.com",
    "https://www.ebay.com",
    "https://www.alibaba.com",
    "https://www.walmart.com",
    "https://www.flipkart.com",
    "https://www.rakuten.com",
    "https://www.shopify.com",
    "https://www.mercadolibre.com",
    "https://www.target.com",
    "https://www.cnn.com",
    "https://www.bbc.com",
    "https://www.nytimes.com",
    "https://www.theguardian.com",
    "https://www.foxnews.com",
    "https://www.aljazeera.com",
    "https://www.bloomberg.com",
    "https://www.cnbc.com",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.techcrunch.com",
    "https://www.wired.com",
    "https://www.theverge.com",
    "https://www.cnet.com",
    "https://arstechnica.com",
    "https://www.engadget.com",
    "https://www.mashable.com",
    "https://www.gizmodo.com",
    "https://www.youtube.com",
    "https://www.netflix.com",
    "https://www.hulu.com",
    "https://www.primevideo.com",
    "https://www.disneyplus.com",
    "https://www.hbomax.com",
    "https://www.spotify.com",
    "https://www.apple.com/music",
    "https://www.soundcloud.com",
    "https://www.twitch.tv",
    "https://www.coursera.org",
    "https://www.khanacademy.org",
    "https://www.edx.org",
    "https://www.udacity.com",
    "https://www.udemy.com",
    "https://www.codecademy.com",
    "https://ocw.mit.edu",
    "https://online-learning.harvard.edu",
    "https://www.futurelearn.com",
    "https://www.booking.com",
    "https://www.airbnb.com",
    "https://www.kayak.com",
    "https://www.skyscanner.com",
    "https://www.agoda.com",
    "https://www.lonelyplanet.com",
    "https://www.paypal.com",
    "https://www.stripe.com",
    "https://www.squareup.com",
    "https://www.robinhood.com",
    "https://www.mint.com",
    "https://www.bankofamerica.com",
    "https://www.wellsfargo.com",
    "https://www.chase.com",
    "https://www.mayoclinic.org",
    "https://www.healthline.com",
    "https://medlineplus.gov",
    "https://www.myfitnesspal.com",
    "https://www.fitbit.com",
    "https://www.strava.com",
    "https://www.nike.com/ntc-app",
    "https://www.onepeloton.com",
    "https://www.foodnetwork.com",
    "https://www.epicurious.com",
    "https://www.bonappetit.com"
    "https://en.wikipedia.org/wiki/Main_Page",
    "https://stackoverflow.com",
    "https://www.khanacademy.org",
    "https://www.nationalgeographic.com",
    "https://archive.org/details/public-domain-archive",
    "https://openlibrary.org",
    "https://gutenberg.org",
    "https://www.ted.com/talks",
    "https://www.codecademy.com",
    "https://www.coursera.org",
    "https://www.udemy.com",
    "https://www.grammarly.com",
    "https://www.si.edu/home",
    "https://spotthestation.nasa.gov/tracking_map.cfm"
    "https://www.reddit.com",
    "https://data.gov",
    "https://www.kaggle.com/datasets",
    "https://www.propublica.org",
    "https://wayback-api.archive.org",  
    "https://world.openfoodfacts.org"
    "https://www.nih.gov/",
    "https://plos.org/",
    "https://arxiv.org/",
    "https://science.nasa.gov/climate-change/",
    "https://data.world/",
    "https://librivox.org/"
    ] 
     
# Connecting MySQL
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="asinbox",
    database="website_data"
)
cursor = db.cursor()

#meta title and description
def get_meta_data(soup):
    meta_title = soup.title.string if soup.title else ''
    meta_description = ''
    if soup.find('meta', attrs={'name': 'description'}):
        meta_description = soup.find('meta', attrs={'name': 'description'}).get('content')
    elif soup.find('meta', attrs={'property': 'og:description'}):
        meta_description = soup.find('meta', attrs={'property': 'og:description'}).get('content')
    return meta_title, meta_description

# ocial media links
def get_social_media_links(soup):
    social_media_links = []
    social_media_platforms = ['facebook', 'twitter', 'linkedin', 'instagram', 'tiktok', 'youtube', 'pinterest']
    for link in soup.find_all('a', href=True):
        if any(platform in link['href'] for platform in social_media_platforms):
            social_media_links.append(link['href'])
    return ', '.join(social_media_links)

#payment gateways
def get_payment_gateways(text):
    payment_gateways = ['paypal', 'stripe', 'razorpay', 'square', 'braintree']
    found_gateways = [gateway for gateway in payment_gateways if gateway in text.lower()]
    return ', '.join(found_gateways)

# tech-stack
def get_tech_stack(soup):
    tech_stack = []
    if soup.find('script', attrs={'src': re.compile(r'.*jquery.*')}):
        tech_stack.append('jQuery')
    if soup.find('script', attrs={'src': re.compile(r'.*react.*')}):
        tech_stack.append('React')
    if soup.find('script', attrs={'src': re.compile(r'.*angular.*')}):
        tech_stack.append('Angular')
    return ', '.join(tech_stack)

#detect website language
def get_website_language(soup):
    if soup.find('html'):
        return soup.find('html').get('lang', '')
    return ''

#categorize website
def categorize_website(url):
    if 'news' in url:
        return 'News and Media'
    if 'shop' in url or 'store' in url:
        return 'E-commerce'
    return 'Others'

#scrape data from website
def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'lxml')
        
        meta_title, meta_description = get_meta_data(soup)
        social_media_links = get_social_media_links(soup)
        payment_gateways = get_payment_gateways(response.text)
        tech_stack = get_tech_stack(soup)
        website_language = get_website_language(soup)
        category = categorize_website(url)

        # Insert data into MySQL database
        cursor.execute("""
            INSERT INTO website_info (url, social_media_links, tech_stack, meta_title, meta_description, payment_gateways, website_language, category)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (url, social_media_links, tech_stack, meta_title, meta_description, payment_gateways, website_language, category))
        db.commit()
        print(f"Data inserted for {url}")
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")

# scrape each website in the list
for website in websites:
    scrape_website(website)

#closing the database connection
cursor.close()
db.close()
