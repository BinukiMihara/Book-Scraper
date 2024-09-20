from bs4 import BeautifulSoup
import requests

try:
    # URL for Books to Scrape website
    url = 'https://books.toscrape.com/'

    # Define headers with User-Agent to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }

    # Make the request with the headers
    source = requests.get(url, headers=headers)
    source.raise_for_status()  # Raises an exception for 4xx/5xx errors

    # Parse the HTML content
    soup = BeautifulSoup(source.text, 'html.parser')

    books = soup.find('ol', class_ = "row").find_all('li', class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")
    print(len(books))
    
except Exception as e:
    print(f"Error: {e}")