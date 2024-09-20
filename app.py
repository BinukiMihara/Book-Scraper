from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active    
sheet.title = 'Book Details'
print(excel.sheetnames)
sheet.append(['Book Name', 'Rating', 'Price', 'Stock Availability'])

try:
    
    # Send a GET request to the URL
    source = requests.get('https://books.toscrape.com/')
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

excel.save('Book Details of Books to Scrape website.xlsx')
