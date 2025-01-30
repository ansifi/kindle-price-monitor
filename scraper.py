import requests
from bs4 import BeautifulSoup
from config import AMAZON_URL, USER_AGENT
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_amazon_price():
    headers = {'User-Agent': USER_AGENT}
    try:
        logging.debug(f"Fetching price for {AMAZON_URL}...")
        
        # Send the request to Amazon
        response = requests.get(AMAZON_URL, headers=headers)
        response.raise_for_status()  # Check for request errors
        
        # Log the status code
        # logging.info(f"Response status code: {response.status_code}")
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Log the first 500 characters of the page's HTML for debugging
        # logging.debug(f"Page HTML (first 500 chars): {response.text[:500]}")

        # Try to find the price using different methods
        price_tag = soup.find('span', {'id': 'priceblock_ourprice'}) or \
                    soup.find('span', {'id': 'priceblock_dealprice'}) or \
                    soup.find('span', {'class': 'a-price-whole'})
        
        if price_tag:
            price = price_tag.text.strip().replace('$', '').replace(',', '')
            # logging.info(f"Found price: {price}")
            return float(price)
        else:
            raise ValueError("Price tag not found on the page")
    
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
    except ValueError as e:
        logging.error(f"Value error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    
    return None