from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class InfoSpider(CrawlSpider):
    name = 'info'
    allowed_domains = ['https://www.jumia.co.ke']
    start_urls = ['https://www.jumia.co.ke/electronics/',
                  'https://www.jumia.co.ke/phones-tablets/'
                    ]
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.osh-font-light-arrow-right',)),
             callback="parse_item",
             follow=True),)
    def parse_item(self, response):
        print('Processing..' + response.url)
