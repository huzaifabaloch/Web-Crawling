import scrapy 
from scrapy_splash import SplashRequest
import csv


class AppSpider(scrapy.Spider):
    name = 'app'
    with open("BarbersData.csv","a") as f:
        writer = csv.writer(f)
        writer.writerow(['Category','Name','Phone','Street Address','Locality','Region','Postal Code'])
 
    allowed_domains = ['truelocal.com.au']
    start_urls = ['https://www.truelocal.com.au/search/barbers/vic']
 
    urls = ['https://www.truelocal.com.au/search/barbers/vic']
 
    def start_requests(self):
        for url in self.urls:
            yield SplashRequest(url,callback=self.parse,args={'wait':'5'})
 
    def parse(self, response):
        links = response.xpath('.//*[@class="item-title"]/@href').extract()
        for link in links:
            yield SplashRequest(link,callback=self.getdata,args={'wait':'5'})
 
        nextlink = response.xpath('.//*[@rel="next"]/@href').extract_first()
        if nextlink:
            yield SplashRequest(nextlink,callback=self.parse,args={'wait':'5'})
 
    def getdata(self,response):
        category = response.xpath('.//div/@ng-click[contains(.,"searchByCategoryName")]/../text()').extract_first()
        name = response.xpath('.//h1/@ng-bind-html[contains(.,"generateName")]/../text()').extract_first()
        phone = response.xpath('.//*[@class="phone ng-scope"]/span/text()').extract_first()
        streetaddress = response.xpath('.//*[@itemprop="streetAddress"]/text()').extract_first()
        locality = response.xpath('.//*[@itemprop="addressLocality"]/text()').extract_first()
        region = response.xpath('.//*[@itemprop="addressRegion"]/text()').extract_first()
        postalcode = response.xpath('.//*[@itemprop="postalCode"]/text()').extract_first()
 
        with open("BarbersData.csv","a") as f:
            writer = csv.writer(f)
            writer.writerow([category,name,phone,streetaddress,locality,region,postalcode])
            print([category,name,phone,streetaddress,locality,region,postalcode])