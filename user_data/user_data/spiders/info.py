from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class InfoSpider(CrawlSpider):
    name = 'info'
    allowed_domains = ['www.jumia.co.ke']
    start_urls = ['https://www.jumia.co.ke/phones-tablets/',
                    'https://www.jumia.co.ke/electronics/',
                    'https://www.jumia.co.ke/grocery/',
                    'https://www.jumia.co.ke/fashion/',
                    'https://www.jumia.co.ke/automobile/',
                    'https://www.jumia.co.ke/video-games/',
                    'https://www.jumia.co.ke/home-office/',
                    'https://www.jumia.co.ke/computing/',
                    'https://www.jumia.co.ke/baby-products/',
                    'https://www.jumia.co.ke/health-beauty/',

                    ]
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.item',)),
             callback="parse_item",
             follow=True),)
    def parse_item(self, response):
        import pdb;
        # pdb.set_trace()
        print('Processing.....' + response.url)
        print("....")
        print("...")
        print("..")
        print(".")
