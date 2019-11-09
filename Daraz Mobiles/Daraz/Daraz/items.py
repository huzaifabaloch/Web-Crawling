import scrapy


class DarazItem(scrapy.Item):

    name = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    image_url = scrapy.Field()