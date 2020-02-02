"""Page Parser module."""
from bs4 import BeautifulSoup
from locators.quote_locator import QuoteLocator

import requests


class PageParser():
    """Define the locators for webscraping."""

    def __init__(self):
        """Define the locators for webscraping."""
        pass

    def get_quotes_page_html(self):
        """Get data from page."""
        self.page = requests.get("http://quotes.toscrape.com/")
        self.soup = BeautifulSoup(self.page.content, "html.parser")

        self.html_data = self.soup.select(QuoteLocator().QUOTE_PAGE_LOCATOR)

        return self.html_data
