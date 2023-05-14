import scrapy
from bs4 import BeautifulSoup

class HomepagesSpider(scrapy.Spider):
    name = "homepages"
    allowed_domains = ["python.org"]
    start_urls = ["https://pypi.org/project/pandas/", "https://pypi.org/project/unstructured/"]
    filename = f"output/crawl2.txt"
    outputdir = "output"
    homepage = ""

    def start_requests(self):
        urls = self.start_urls # Replace with your desired website
        
        for url in urls:
            self.homepage=url.split("//")[1].replace("/","_")
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = self.homepage
        self.filename = f"output/{page}.txt"
        
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        text = '\n'.join([line.strip() for line in text.split('\n') if line.strip()])
        
        
        with open(self.filename, 'a') as f:
            f.write(text)
        self.log(f'Saved file {self.filename}')

        for link in response.css('a::attr(href)').getall():
            yield response.follow(link, self.parse)
