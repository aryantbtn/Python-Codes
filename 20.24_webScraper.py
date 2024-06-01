# Web scraper with Python
# In this article, I'mng to create a web scraper with Python that pulls all the stories from Google News by extracting all the tags from the HTML of Google News.

import urllib.request
from bs4 import BeautifulSoup
class scraper:
    def __init__(self, site):
        self.site = site
    def scrape(self):
        aryan = urllib.request.urlopen(self.site)
        html = aryan.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            href = tag.get("href") # Hyperlink
            if href is None:
                continue
            if "articles" in href:
                print("\n" + href)
news = "https://news.google.com/"
scraper(news).scrape()