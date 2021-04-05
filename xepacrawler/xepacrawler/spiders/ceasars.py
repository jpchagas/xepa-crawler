import scrapy


class CeasarsSpider(scrapy.Spider):
    name = 'ceasars'
    allowed_domains = ['http://ceasa.rs.gov.br/']
    start_urls = ['http://ceasa.rs.gov.br/tabcotacao/02-03-2021/']

    def parse(self, response):
        pass
