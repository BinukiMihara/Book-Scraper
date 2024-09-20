# Book-Scraper

This Python project scrapes book details from the [Books to Scrape](http://books.toscrape.com/) website and saves the extracted data into an Excel file using `openpyxl`.

## Features

- Scrapes book names, ratings, prices, and stock availability from the website.
- Stores the scraped data in an Excel file (`Book Details of Books to Scrape website.xlsx`).
- Uses the `requests` and `BeautifulSoup` libraries to fetch and parse the webpage.
- Automatically creates an Excel workbook and writes the scraped data into it.

## Prerequisites

Make sure you have the following libraries installed in your Python environment:

- `requests`
- `beautifulsoup4`
- `openpyxl`
  
## How to Run
- Clone or download this repository.
- Install the required libraries.
- Run the app.py script to start scraping the book details.
- After running the script, an Excel file named Book Details of Books to Scrape website.xlsx will be created in the project folder with the scraped book details.
```bash
Copy code

pip install requests beautifulsoup4 openpyxl
python app.py


