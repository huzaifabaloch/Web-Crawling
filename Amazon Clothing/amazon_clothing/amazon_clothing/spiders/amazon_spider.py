import scrapy
from ..items import AmazonClothingItem

class Amazon(scrapy.Spider):

    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A2476517011&lo=visual_grid&dc&page=1&_encoding=UTF8&qid=1565958377&rnid=1040658&ref=sr_pg_2'
    ]
    page_number = 2

    def parse(self, response):

        items = AmazonClothingItem()
    
        product_box = response.css('.s-include-content-margin')

        for each_product in product_box:
            product_name = each_product.css('.a-size-base-plus.a-color-base.a-text-normal::text').extract()
            manufacturer = each_product.css('div.a-row.a-size-base.a-color-secondary span.a-size-base::text').extract()
            price = each_product.css('div.a-row a.a-size-base.a-link-normal.s-no-hover.a-text-normal span.a-price span.a-price-whole::text').extract()

            items['product_name'] = product_name[0]

            if len(manufacturer) == 2:
                items['product_manufacturer'] = manufacturer[1]
            else:
                items['product_manufacturer'] = ''

            if len(price) == 2:
                items['product_starting_price'] = price[0]
                items['product_ending_price'] = price[1]
            elif len(price) == 1:
                items['product_starting_price'] = price[0]
                items['product_ending_price'] = ''
            else:
                items['product_starting_price'] = ''
                items['product_ending_price'] = ''

            yield items

        next_page = 'https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A2476517011&lo=visual_grid&dc&page=' + str(Amazon.page_number) + '&_encoding=UTF8&qid=1565958377&rnid=1040658&ref=sr_pg_2'
        if Amazon.page_number < 6:
            Amazon.page_number += 1
            yield response.follow(next_page, callback=self.parse)


           