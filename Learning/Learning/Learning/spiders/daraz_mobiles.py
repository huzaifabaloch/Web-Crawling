import scrapy
from scrapy_splash import SplashRequest


class DarazMobile(scrapy.Spider):

    name = 'darazMobile'
    allowed_domains = ['daraz.pk']
    start_urls = ['https://www.daraz.pk/smartphones/?page=1&spm=a2a0e.home.cate_1.1.35e34937UIUU2F']
    page_number = 2
    #handle_httpstatus_list = [500, 502, 504]
    link_number = 1
    links = []

    def start_requests(self):
        yield SplashRequest(
            url=self.start_urls[-1],
            callback=self.parse,
            errback=self.start_requests,
            args={'wait': 10},
            #meta={"proxy": "199.114.221.40:8080"},
        )

    def parse(self, response):

        if not self.links:
            url_container = response.css('div.c2prKC')
            for each_url in url_container.css('div.cRjKsc a::attr(href)').extract():
                self.links.append('https:' + each_url)

        for link_number, each_link in enumerate(self.links, start=self.link_number):
            yield SplashRequest(
                url=each_link,
                callback=self.parse_details,
                errback=self.error_back_504,
                args={'wait': 12},
                #meta={"proxy": "199.114.221.40:8080"},
            )

        next_page = 'https://www.daraz.pk/smartphones/?page=' + str(self.page_number) + '&spm=a2a0e.home.cate_1.1.35e34937UIUU2F'
        if self.page_number < 85:
            self.page_number += 1
            yield SplashRequest(
                url=next_page,
                callback=self.parse,
                args={'wait': 10},
                #meta={"proxy": "199.114.221.40:8080"},
            )
    
    def error_back_504(self, failure):
        print(failure)


    def parse_details(self, response):

        product_name = response.css('div.pdp-mod-product-badge-wrapper span::text').extract_first()
        product_price = response.css('div.pdp-product-price span::text').extract_first()
        product_brand = response.css('div.pdp-product-brand a::text').extract_first()
        ratings = response.css('a.pdp-link.pdp-link_size_s.pdp-link_theme_blue.pdp-review-summary__link::text').extract_first()
        stars = response.css('div.score span::text').extract_first()

        yield {
            'product_name': product_name,
            'product_price': product_price,
            'product_brand': product_brand,
            'rating': ratings,
            'star': stars,
        }
        
        
