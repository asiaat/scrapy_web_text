import scrapy


class HomepagesSpider(scrapy.Spider):
    name = "homepages"
    allowed_domains = ["python.org"]
    start_urls = ["http://python.org/"]

    def start_requests(self):
        urls = self.start_urls # Replace with your desired website
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"{page}.txt"
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        for link in response.css('a::attr(href)').getall():
            yield response.follow(link, self.parse)
