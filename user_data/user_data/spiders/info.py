# -*- coding: utf-8 -*-
import scrapy


class InfoSpider(scrapy.Spider):
    name = 'info'
    allowed_domains = ['www.facebook.com']
    start_urls = ['http://www.facebook.com/']

    def parse(self, response):
        pass
