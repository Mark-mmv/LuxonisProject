import scrapy


class SrealityApartmentsSpider(scrapy.Spider):
    name = 'sreality_apartments'
    allowed_domains = ['sreality.cz']
    start_urls = ['http://sreality.cz/']

    def parse(self, response):
        pass
