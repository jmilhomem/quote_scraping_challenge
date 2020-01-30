"""Class with parsers' definitions."""
from locators.quote_locator import QuoteLocator


class Parser():
    """Define the locators for webscraping."""

    def __init__(self, content_data):
        """Define the content."""
        self.content = content_data
        #return self.content

    def __repr__(self):
        """Return a print of results."""
        return f"{self.author}"
        #return f"Quote {self.quote_content}, by {self.author}, tags: {self.tags}"

    @property
    def author(self):
        """Return the author data."""
        locator = QuoteLocator.AUTHOR_LOCATOR
        print(self.content.select_one(locator).string)
        return self.content.select_one(locator.string)

    #@property
    #def quote_content(self):
        """Return the quote content data."""
    #    locator = QuoteLocator.QUOTE_LOCATOR
    #    return self.content.select_one(locator)

    #@property
    #def tags(self):
        """Return the tags data."""
    #    locator = QuoteLocator.TAG_LOCATOR
    #    return [tag.string for tag in self.content.select(locator)]
