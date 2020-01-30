from bs4 import BeautifulSoup
from parser_ import quote_parser
from locators.quote_locator import QuoteLocator

import requests


page = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(page.content, "html.parser")

html_data = soup.select(QuoteLocator().QUOTE_PAGE_LOCATOR)


"""Get data from each block of html."""
for content_html in enumerate(html_data):
    pos_data = content_html[0]

    data_content = quote_parser.Parser(content_html[1])
    pos_data = pos_data + 1

    print(f"{pos_data} - {data_content}")
