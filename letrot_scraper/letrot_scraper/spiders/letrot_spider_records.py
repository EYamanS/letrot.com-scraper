import scrapy
import json

class LetrotSpiderRecordsSpider(scrapy.Spider):

    name = 'letrot_spider_records'
    allowed_domains = ['www.letrot.com']
    start_urls = []

    data = json.load(open('devFiles/result2.json','r'))

    for obj in data:
        start_urls.append(obj['course_link'])





    def parse(self, response):
        pass
