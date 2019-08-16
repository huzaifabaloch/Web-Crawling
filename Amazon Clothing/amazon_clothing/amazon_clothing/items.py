# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonClothingItem(scrapy.Item):

    product_name = scrapy.Field()
    product_manufacturer = scrapy.Field()
    product_starting_price = scrapy.Field()
    product_ending_price = scrapy.Field()