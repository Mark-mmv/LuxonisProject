import scrapy
import json
from unicodedata import normalize
from items import SrealityparserItem

class SrealityApartmentsSpider(scrapy.Spider):
    name = 'sreality_apartments'
    allowed_domains = ['sreality.cz']
    start_urls = ['http://sreality.cz/']

    def start_requests(self):
        url = f"https://www.sreality.cz/api/en/v2/estates?category_main_cb=1&category_type_cb=1&sort=0&per_page=500"
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        jsonresponse = json.loads(response.body)

        for item in jsonresponse["_embedded"]["estates"]:
            apartment = SrealityparserItem()
            apartment["name"] = normalize('NFKD', item['name'])
            apartment["locality"] = item["locality"]
            apartment["price"] = int(float(item["price_czk"]["value_raw"]) * 0.791525)
            apartment["img_url"] = item["_links"]["images"][0]["href"]
            yield apartment

