import scrapy 


class Proxy(scrapy.Spider):

    """
        * The way it works is that inside Scrapy, there’s a middleware called HttpProxyMiddleware 
        * which takes the proxy meta parameter from the request object and sets it up correctly as the used proxy. 
        * The middleware is enabled by default so there is no need to set it up.
    """

    name = 'proxyBot'

    start_urls = ['https://www.whatismyip.com/']

    def start_requests(self):

        for _url in self.start_urls:
            yield scrapy.Request(
                url=_url,
                callback=self.parse, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'},
                meta={"proxy": "199.114.221.40:8080"},
                )

    def parse(self, response):

        proxy = response.css('ul.list-group.text-center li::text').extract()
        
        yield {
            '1.': proxy[0].strip(),
            '2.': proxy[1].strip(),
            '3.': proxy[2].strip(),
        }