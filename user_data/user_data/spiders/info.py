from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class InfoSpider(CrawlSpider):
    name = 'info'
    allowed_domains = ['https://www.jumia.co.ke']
    start_urls = ['https://www.jumia.co.ke/electronics/',
                  'https://www.jumia.co.ke/phones-tablets/'
                    ]
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.item',)),
             callback="parse_item",
             follow=False),)
    def parse_item(self, response):
        print('Processing..' + response.url)
