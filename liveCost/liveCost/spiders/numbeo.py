# -*- coding: utf-8 -*-
import scrapy


class NumbeoSpider(scrapy.Spider):
    name = 'numbeo'
    allowed_domains = ['numbeo.com/cost-of-living/']
    start_urls = ['http://numbeo.com/cost-of-living//']

    def parse(self, response):
        pass
