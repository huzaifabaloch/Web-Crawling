import scrapy 
from scrapy_splash import SplashRequest


class Daraz_B(scrapy.Spider):

    name = 'botB'
    #allowed_domains = ['daraz.pk']
    start_urls = ['https://www.daraz.pk/products/tecno-camon-12-air-64gb-rom-4gb-ram-655-punch-hole-display-i128384065-s1287447428.html?search=1',
    'https://www.daraz.pk/products/tecno-camon-12-air-64gb-rom-4gb-ram-655-punch-hole-display-i128384065-s1287447428.html?search=1',
'https://www.daraz.pk/products/gfive-king-3-sim-huge-battery-3600-mah-24-big-display-1-year-warranty-bluetooth-camera-multilanguag-i115498717-s1267438413.html?search=1',
'https://www.daraz.pk/products/nokia-105-2019-17-inch-display-2000-contact-500-sms-i116606109-s1268754753.html?search=1',
'https://www.daraz.pk/products/new-nokia-106-2018-dual-sim-high-quality-keypad-2000-contact-i101645270-s1247181471.html?search=1',
'https://www.daraz.pk/products/gfive-mobile-phone-free-delivery-tiger-1200-mah-battery-18-display-double-sim-camera-bluetooth-approved-by-pta-any-color-i128737595-s1288061274.html?search=1',
'https://www.daraz.pk/products/etachi-e4-triple-sim-mobile-phone-big-battery-any-color-i121926135-s1277918476.html?search=1',
'https://www.daraz.pk/products/gaesso-a10-28-triple-sim-i121788179-s1277686571.html?search=1'
    ]
    
    def start_requests(self):
    
        '''with open('links.txt', 'r') as fileOpen:
            text = fileOpen.read()
            links = text.split('')
            del links[-1]

            for each_link in links:
                if '//' in each_link:
                    self.start_urls.append(each_link.replace('//', ''))'''

        for each_url in self.start_urls:
            yield SplashRequest(
                url=each_url,
                callback=self.parse,
                args={'wait': 10},
            )

    def parse(self, response):
        
        product_name = response.css('div.pdp-product-price span.pdp-price.pdp-price_type_normal.pdp-price_color_orange.pdp-price_size_xl').extract_first()
        yield {'Name': product_name}
            