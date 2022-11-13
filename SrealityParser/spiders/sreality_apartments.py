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
              f"{self.count}"
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        jsonresponse = json.loads(response.text)
        for item in jsonresponse["_embedded"]["estates"]:
            yield scrapy.Request(
                'https://www.sreality.cz/api' + item['_links']['self']['href'], callback=self.parser_apartment)

    def parser_apartment(self, response):
        jsonresponse = json.loads(response.text)
        apartment = SrealityparserItem()
        apartment["name"] = jsonresponse["name"]["value"]
        apartment["locality"] = jsonresponse["locality"]["value"]
        apartment["price"] = jsonresponse["price_czk"]["value_raw"]
        for imgs in jsonresponse["_embedded"]["images"]:
            if imgs["_links"]["view"]:
                apartment["img_url"] = imgs["_links"]["view"]["href"]
                break
        yield apartment

