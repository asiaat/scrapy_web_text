import scrapy


class HomepagesSpider(scrapy.Spider):
    name = "homepages"
    allowed_domains = ["python.org"]
    start_urls = ["http://python.org/"]

    def parse(self, response):
        pass
