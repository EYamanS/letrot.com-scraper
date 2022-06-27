import json
import scrapy


class LetrotXpathSpiderSpider(scrapy.Spider):

    name = 'meetings-spider'
    allowed_domains = ['www.letrot.com']
    start_urls = ['https://www.letrot.com/en/races/calendar-results']



    def parse(self, response):

        result_file_name = "meetings"
        result_file_handle = open(f"results/{result_file_name}.csv","w")

        meetings = []


        with open('devFiles/latest_response.html','w') as fh:
            fh.write(response.text)


        for reunionTypeHolder in response.xpath('//div[@class="reunionType"]'):
            links =  reunionTypeHolder.xpath('./a')

            for link in links:
                link_href = link.xpath('@href').extract()[0]
                link_name = link.xpath('string(.)').extract()[0].strip()
                """/stats/courses/programme/2022-07-27/0601"""
                link_date = link_href.split("/")[4]


                meetings.append(
                    {
                        "name": link_name,
                        "href": link_href,
                        "date": link_date
                    }
                )



        for meet in meetings:
            with open('devFiles/result1.json','a') as rf:
                json.dump(meet,rf)
                rf.write("\n")

        meet_normals = [{
            "name": meet['name'],
            "date": meet['date']
        } for meet in meetings]

        for meet in meet_normals:     
            with open('results/meetings.json','a') as rf:
                json.dump(meet,rf)
                rf.write("\n")
        
        attrs = ["Hippodrome","Date"]

        result_file_handle.write(",".join(attrs)+"\n")
        for line in open("devFiles/result1.json","r").readlines():
            obj = json.loads(line)
            result_file_handle.write(f"{obj['name']},{obj['date']}"+"\n")