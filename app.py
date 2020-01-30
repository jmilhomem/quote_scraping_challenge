from bs4 import BeautifulSoup
from parser_ import quote_parser
from locators.quote_locator import QuoteLocator

import requests


page = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(page.content, "html.parser")


print("LOCATOR", QuoteLocator().QUOTE_PAGE_LOCATOR)
#soup.select(quote_page_locator)

TEST = soup.select(QuoteLocator().QUOTE_PAGE_LOCATOR)
#print("1.", TEST)

TEST2 = quote_parser.Parser(TEST)
print("2.", TEST2)

"""
# Get data from each block of html
for content_html in soup.select(quote_page_locator.QUOTE_PAGE_LOCATOR):
    # print(content_html)

    quote_parser(content_html)

print("******************************\n")
"""