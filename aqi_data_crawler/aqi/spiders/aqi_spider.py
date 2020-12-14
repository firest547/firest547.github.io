from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from aqi.items import AqiItem
import logging


class AQISpider(CrawlSpider):
    name = "aqi"
    allowed_domains = ['data.ec.gc.ca']
    start_urls = [
        'http://data.ec.gc.ca/data/air/monitor/national-air-pollution'
        '-surveillance-naps-program/Data-Donnees/?lang=en',
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'data\/air\/monitor\/national\-air\-'
                                  r'pollution\-surveillance\-naps\-program'
                                  r'\/Data\-Donnees\/[0-9]',),
                           deny=('#shr\-pg0', 'lang\=fr', 'index\.html')),
             follow=True, callback='parse_item'),
    )

    def parse_item(self, response):
        file_url = response.url
        file_extension = file_url.split('.')[-1]
        if file_extension in ('xls', 'txt', 'json', 'csv', 'zip'):
            logging.info('Parsing: ' + response.url)
            yield AqiItem(file_urls=[response.urljoin(file_url)])
