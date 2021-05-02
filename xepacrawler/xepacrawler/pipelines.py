import requests
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class XepacrawlerPipeline:
    def process_item(self, item, spider):
        payload = {'release_date':item['data'][0],
                       'product':item['produto'][0],
                       'unit':item['unidade'][0],
                       'max_value':item['maximo'][0],
                       'frequent_value':item['frequente'][0],
                       'min_value':item['minimo'][0]}
        requests.post('http://127.0.0.1:5000/price', json=payload)
        return item
