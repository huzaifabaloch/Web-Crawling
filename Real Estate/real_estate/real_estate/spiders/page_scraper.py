from bs4 import BeautifulSoup
from requests import get


class Scraper():

    def __init__(self, link):

        self.link = link
        self.response = get(self.link, headers='Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
        self.soup = ''

    def to_scrape(self):

        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        print("YES")
