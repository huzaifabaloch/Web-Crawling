# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealEstateItem(scrapy.Item):
    """
     This class is responsible to store the data from website of each field in a 
     temporary containers.
    """
    
    # Defining the fields for the website that spider will crawl and scrape.
    estate_name = scrapy.Field()
    home = scrapy.Field()
    plot = scrapy.Field()
    commercial = scrapy.Field()
    rental = scrapy.Field()
    contact_person = scrapy.Field()
    city = scrapy.Field()
    address = scrapy.Field()
    proprietor = scrapy.Field()
    phone_number = scrapy.Field()
