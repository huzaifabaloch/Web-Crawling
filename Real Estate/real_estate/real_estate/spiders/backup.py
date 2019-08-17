# -*- coding: utf-8 -*-
import scrapy
import real_estate.spiders.page_scraper as r
from ..items import RealEstateItem


class HomePakistanSpider(scrapy.Spider):
    """
     This class contain name of spider and set of urls that spider will crawl on internet.
     The scrapy.Spider class is inherited that contains many functionalities that we dont need to include.
     Also scrapy.Spider class expects us to have spider name and start urls.
    """

    name = 'homebot'
    start_urls = [
        'https://www.homespakistan.com/?p=1&page=agents_feature&user_cityId=0&user_areaId=0&alpha=&name=&record_per_page=15'
    ]
    page_number = 2

    def scrape_page(self, response):

        items = RealEstateItem()

        title = response.css('div.col-sm-9 h2.green-heading::text').extract_first()
        property_details = response.css('div.box-border a h2::text').extract()
        developer_details = response.css('div.developer-detail h4::text').extract()

        home = property_details[0].strip()
        plot = property_details[1].strip()
        commercial = property_details[2].strip()
        rental = property_details[3].strip()
        contact_person = developer_details[0].strip()
        proprietor = developer_details[1].strip()
        city = developer_details[2].strip()
        
        if developer_details[3][:3] == '+92':
            if '\xa0' in developer_details[3]:
                phone = developer_details[3].replace('\xa0','')
                phone = phone[:13]
            else:
                phone = developer_details[3][:13]

        elif developer_details[3][:4] == '0092':
            if '\xa0' in developer_details[3]:
                phone = developer_details[3].replace('\xa0','')
                phone = phone[:14]
            else:
                phone = developer_details[3][:14]

        elif developer_details[3][:2] == '92':
            if '\xa0' in developer_details[3]:
                phone = developer_details[3].replace('\xa0','')
                phone = phone[:12]
            else:
                phone = developer_details[3][:12]

        elif developer_details[3][:5] == '00971':
            if '\xa0' in developer_details[3]:
                phone = developer_details[3].replace('\xa0','')
                phone = phone[:14]
            else:
                phone = developer_details[3][:14]
        
        elif developer_details[3][:4] == '+971':
            if '\xa0' in developer_details[3]:
                phone = developer_details[3].replace('\xa0','')
                phone = phone[:13]
            else:
                phone = developer_details[3][:13]

        elif developer_details[3][:3] == '971':
            if '\xa0' in developer_details[3]:
                phone = developer_details[3].replace('\xa0','')
                phone = phone[:12]
            else:
                phone = developer_details[3][:12]

        else:
            if '\xa0' in developer_details[3]:
                phone = developer_details[3].replace('\xa0','')
                if '-' in phone:
                    phone = phone.replace('-','')
                    phone = phone[:11]
                else:
                    phone = developer_details[3][:11]
            else:
                if '-' in developer_details[3]:
                    phone = developer_details.replace('-','')
                    phone = phone[:11]
                else:
                    phone = developer_details[3][:11]

        address = developer_details[4].strip()
    
        items['estate_name'] = title
        items['home'] = int(home)
        items['plot'] = int(plot)
        items['commercial'] = int(commercial)
        items['rental'] = int(rental)
        items['contact_person'] = contact_person
        items['proprietor'] = proprietor
        items['city'] = city
        items['phone_number'] = phone
        items['address'] = address

        yield items
        

    def parse(self, response):
        """ 
        The method where spider extract information from HTML based on CSS selectors.
        The scrapy returns response object that contain all the source code of a webpage.
        """

        # Extracting all the links on the page.
        estate_block = response.css('div.list-bg-find.margin-no div.find-agent-left div.btn-see.mobile a::attr(href)').extract()

        # On each iteration the crawler will follow each link.
        for each_link in estate_block:
            yield response.follow(each_link, callback=self.scrape_page)

        next_page = 'https://www.homespakistan.com/?p=' + str(HomePakistanSpider.page_number) + '&page=agents_feature&user_cityId=0&user_areaId=0&alpha=&name=&record_per_page=15'
        if HomePakistanSpider.page_number < 111:
            HomePakistanSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
    