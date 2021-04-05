import scrapy
#from ..items import MarketListCrawlerItem
from scrapy.loader import ItemLoader
import json


class CeasarsSpider(scrapy.Spider):
    name = 'ceasars'
    #allowed_domains = ['http://ceasa.rs.gov.br/']
    #start_urls = ['http://ceasa.rs.gov.br/tabcotacao/02-03-2021/']

    def start_requests(self):
        urls = [
            'http://ceasa.rs.gov.br/tabcotacao/02-03-2021/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        result = {}
        result["dia"] = response.xpath("//header/h1/text()").get()
        dia = response.xpath("//header/h1/text()").get()
        if dia[0] == 'C':
            dia = dia[8:]

        for row in response.xpath('//table/tbody/tr'):
            '''
            l = ItemLoader(item=MarketListCrawlerItem(), selector=row)
            l.add_xpath('produto', "td[1]//text()")
            l.add_xpath('unidade', "td[2]//text()")
            l.add_xpath('maximo', "td[3]//text()")
            l.add_xpath('frequente', "td[4]//text()")
            l.add_xpath('minimo', "td[5]//text()")
            l.add_value('data', dia.replace('/', '-'))
            # l.add_value('data', dh.current_date())
            l.add_value('origem', "CEASARS")
            yield l.load_item()
            '''
            produto = row.xpath('td[1]//text()').extract_first()
            result["produto"] = row.xpath('td[1]//text()').extract_first()
            unidade = row.xpath('td[2]//text()').extract_first()
            result["unidade"] = row.xpath('td[2]//text()').extract_first()
            maximo = row.xpath('td[3]//text()').extract_first()
            result["maximo"] = row.xpath('td[3]//text()').extract_first()
            frequente = row.xpath('td[4]//text()').extract_first()
            result["frequente"] = row.xpath('td[4]//text()').extract_first()
            minimo = row.xpath('td[5]//text()').extract_first()
            result["minimo"] = row.xpath('td[5]//text()').extract_first()

            with open("data_file.json", "w") as write_file:
                json.dump(result, write_file)

            '''
            yield {
                'produto': row.xpath('td[1]//text()').extract_first(),
                'unidade': row.xpath('td[2]//text()').extract_first(),
                'maximo': row.xpath('td[3]//text()').extract_first(),
                'frequente': row.xpath('td[4]//text()').extract_first(),
                'minimo': row.xpath('td[5]//text()').extract_first(),
            }
            '''
