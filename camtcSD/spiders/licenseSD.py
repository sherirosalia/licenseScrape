# -*- coding: utf-8 -*-

import scrapy
import requests
import json
import datetime
import re

class LicensesdSpider(scrapy.Spider):
    name = 'licenseSD'
    #allowed_domains = ['camtc.org/record-search?work=san+diego']
    start_urls = ['https://ws.camtc.org/api/Individual/IndividualSearchPublic/123?FirstName=&LastName=&LicenseNumber=&CityofWork=san%20diego']
    # ['http://https://www.camtc.org/record-search?work=san+diego/']

    def parse(self, response):
         response = response.body
         yield response
