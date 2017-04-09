from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def __init__(self, baseUrl, pageUrl):
        super().__init__()
        self.baseUrl = baseUrl
        self.pageUrl = pageUrl
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.baseUrl, value)
                    self.links.add(url)

    def pageLinks(self):
        return self.links

    def error(self, message):
        pass
