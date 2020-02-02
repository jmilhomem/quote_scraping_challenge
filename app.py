"""App program."""
from parsers import page_parser, quote_parser


def print_quotes(html_data):
    """Get data from each block of html and parse it."""
    for content_html in enumerate(html_data):
        pos_data = content_html[0]

        data_content = quote_parser.Parser(content_html[1])
        pos_data = pos_data + 1

        print(f"{pos_data} - {data_content}")

if __name__ == "__main__":
    page = page_parser.PageParser()
    html_data = page.get_quotes_page_html()
    print_quotes(html_data)
