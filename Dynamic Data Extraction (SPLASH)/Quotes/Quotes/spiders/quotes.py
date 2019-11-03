import scrapy
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):

    name = 'quote'
    
    def start_requests(self):
        yield SplashRequest(url='http://quotes.toscrape.com/js', callback=self.parse)

    def parse(self, response):

        title = response.css('span.text::text').extract()
        print(title)
        