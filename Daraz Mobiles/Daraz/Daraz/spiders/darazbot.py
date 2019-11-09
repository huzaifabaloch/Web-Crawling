import scrapy
from scrapy_splash import SplashRequest
from ..items import DarazItem

class DarazMobile(scrapy.Spider):

    name = 'darazbot'
    #allowed_domains = ['daraz.pk']
    start_urls = ['https://www.daraz.pk/smartphones/?page=1&spm=a2a0e.searchlistcategory.cate_1.1.251b6e5ewErf5V']

    def start_requests(self):
        
        for _url in self.start_urls:
            yield SplashRequest (
                url = _url,
                callback = self.parse,
                args={'wait': 5}
            ) 

    def scrape_data(self, response):

        product_name = response.css('span.pdp-mod-product-badge-title::text').extract_first()
        yield {'Name': product_name}


    
    def parse(self, response):

        links = response.css('div.c16H9d a::attr(href)').extract()

        with open('links.txt', 'w') as fileOpen:
            for each_link in links:
                fileOpen.write(each_link + '\n')

        
            