import json
import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime, timezone




class LetrotXpathSpiderSpider(scrapy.Spider):

    name = 'meetings-spider'
    allowed_domains = ['www.letrot.com']
    start_urls = ['https://www.letrot.com/en/races/calendar-results']



    def parse(self, response):

        result_file_name = "Reunion"
        result_file_handle = open(f"results/{result_file_name}.csv","w")

        meetings = []


        with open('devFiles/latest_response.html','w') as fh:
            fh.write(response.text)


        for reunionTypeHolder in response.xpath('//div[@class="reunionType"]'):
            links =  reunionTypeHolder.xpath('./a')

            for link in links:
                link_href = link.xpath('@href').extract()[0]
                link_id = link.xpath('@id').extract()[0]

                is_premium = 0
                if 'Premium' in link_id:
                    is_premium = 1

                link_name = link.xpath('string(.)').extract()[0].strip()
                """/stats/courses/programme/2022-07-27/0601"""
                link_date = link_href.split("/")[4]

                date_parts = link_date.split('-')

                link_date_formatted = '/'.join([date_parts[2],date_parts[1],date_parts[0][-2:]])

                dt = datetime(int(link_date.split('-')[0]),int(link_date.split('-')[1]),int(link_date.split('-')[2])).timestamp()

                #.lower() if is_premium ==0 else link_name
                meetings.append(
                    {
                        "nom-reunion": link_name + ' ' + link_date_formatted,
                        "href": link_href,
                        'nom-hippodrome': link_name,
                        "date-reunion": dt,
                        'is_premium': is_premium 
                    }
                )



        for meet in meetings:
            with open('devFiles/result1.json','a') as rf:
                json.dump(meet,rf)
                rf.write("\n")

        meet_normals = [{
            "nom-reunion": meet['nom-reunion'],
            "nom-hippodrome": meet['nom-hippodrome'],
            "date-reunion": meet['date-reunion']
        } for meet in meetings]

        for meet in meet_normals:     
            with open('results/meetings.json','a') as rf:
                json.dump(meet,rf)
                rf.write("\n")
        
        attrs = ["nom-reunion","nom-hippodrome","date-reunion"]

        result_file_handle.write(",".join(attrs)+"\n")
        for line in open("devFiles/result1.json","r").readlines():
            obj = json.loads(line)
            '''
            if obj['is_premium'] == 0:
                obj['name'] = obj['name'].lower()
            '''
            result_file_handle.write(f"{obj['nom-reunion']},{obj['nom-hippodrome']},{obj['date-reunion']}"+"\n")




process = CrawlerProcess()
process.crawl(LetrotXpathSpiderSpider)
process.start()
