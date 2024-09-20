from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active    
sheet.title = 'Book Details'
print(excel.sheetnames)
sheet.append(['Name', 'Rating', 'Price', 'Stock'])

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

    for book in books:
        name = book.find('h3').a.text
        #rating = book.find('p', class_ = "star-rating Three")['class'][1]
        rating_tag = book.find('p', class_="star-rating")
        if rating_tag:
            rating = rating_tag['class'][1]  # Second class contains the rating (e.g., "Three", "Four")
        else:
            rating = "No rating"
        price = book.find('div', class_ = "product_price").p.get_text(strip=True).strip('£')[1:]
        stock = book.find('p', class_ = "instock availability").get_text(strip=True).strip('""')
        print(name, rating, price, stock)
        sheet.append([name, rating, price, stock])
        
    
except Exception as e:
    print(f"Error: {e}")

excel.save('books.xlsx')
