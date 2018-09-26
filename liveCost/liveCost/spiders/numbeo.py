# -*- coding: utf-8 -*-
import scrapy


class NumbeoSpider(scrapy.Spider):
    name = 'numbeo'
    allowed_domains = ['numbeo.com/cost-of-living/']
    start_urls = ['http://numbeo.com/cost-of-living/']
    # rules = (Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),callback="parse_item",follow=True),)
    def parse(self, response):
        print('Processing..' + response.url)
