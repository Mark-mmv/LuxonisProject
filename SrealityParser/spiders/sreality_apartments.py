import scrapy
import json
from SrealityParser.items import SrealityparserItem

class SrealityApartmentsSpider(scrapy.Spider):
    name = 'sreality_apartments'
    allowed_domains = ['sreality.cz']
    start_urls = ['http://sreality.cz/']
    count = 5

    def start_requests(self):
        url = f"https://www.sreality.cz/api/en/v2/estates?category_main_cb=1&category_type_cb=1&sort=0&per_page=" \
              f"{self.count+1}"
        yield scrapy.Request(url, callback=self.parse)
    def parse(self, response):
        pass
