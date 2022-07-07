import scrapy
import json
from scrapy.crawler import CrawlerProcess



class LetrotSpiderRecordsSpider(scrapy.Spider):

    name = 'letrot_spider_records'
    allowed_domains = ['www.letrot.com']
    start_urls = []

    data = json.load(open('devFiles/result2.json','r'))

    for obj in data:
        if 'tableau' in obj['course_link']:
            obj['course_link'] += '#sub_sub_menu_course'
        if 'arrivee-definitive' in obj['course_link']:
            obj['course_link'] = obj['course_link'].strip('resultats/arrivee-definitive')
            obj['course_link'] += '/partants/tableau#sub_sub_menu_course'
        start_urls.append(obj['course_link'])


    def parse(self, response):
        
        result_table = response.xpath('//tbody')
        
        for row in result_table.xpath('./tr'):
            row_infos = row.xpath('./td')
            for info in row_infos:
                info_class = info.xpath('@class').extract()
                self.log(type(info_class))
                if info_class == 'nowrap other-fixed-colomn':
                    record_cheval = info.xpath('@text').extract()
                    self.log(record_cheval)



process = CrawlerProcess()
process.crawl(LetrotSpiderRecordsSpider)
process.start()
