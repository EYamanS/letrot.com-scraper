from typing import Counter
import scrapy
import json
import requests
import time
from scrapy.crawler import CrawlerProcess
import os

with open('devFiles/result2.json','w') as fh:
    fh.write('')



class LetrotSpiderCoursesSpider(scrapy.Spider):
    name = 'letrot_spider_courses'
    allowed_domains = ['www.letrot.com']
    start_urls = ["https://www.letrot.com/"+json.loads(line)["href"]+'/json' for line in open('devFiles/result1.json','r').readlines()]


    counter = 0
    attrs = ['Nom','Prix',"Distance","Mode course","Conditions","Depart"]

    with open('devFiles/result2.json','w') as  fh:
        fh.write('[]')

    def parse(self, response):

        '''https://www.letrot.com/stats/courses/programme/2022-06-27/1400'''
        current_url = response.request.url
        courses = []



        self.counter = 0
        responseObj = json.loads(response.text)
        course_responses = [course for course in responseObj['course']]
        course_name = responseObj['nomHippodrome']
        '''
        for line in open('devFiles/result1.json','r').readlines():
            if course_name in line or course_name.lower() in line:
                if current_url.strip('https://www.letrot.com/').strip('/json') in line:
                    course_name = line.split(':')[1].split(',')[0].strip().strip('"')
        '''

        '''2022-06-30'''
        date = current_url.split('/')[7]
        date_parts = date.split('-')

        date = '/'.join([date_parts[2],date_parts[1],date_parts[0][-2:]])


        for course_response in course_responses:

            self.counter += 1


            course_obj = {
                'nom-course': course_name+' '+date+' C'+str(course_response['numCourse']),
                'prix-course': str(course_response['allocation']) + 'E',
                'distance-course': str(course_response['distance']+'m'),
                'mode-course': str(course_response['discipline']),                                      
                'condition-course': str(course_response['conditionsEngagement']).replace('<br />',' ').replace("D\u00e9part \u00e0 l'autostart",' '),
                'course_link': str(course_response['linkPrix']),
                'depart-course': 'Volte' if 'autostart' not in str(course_response['conditionsEngagement']) else 'Autostart',
                '_got_from': response.request.url
            }


            for key in course_obj:
                if ',' in course_obj[key]:
                    course_obj[key] = course_obj[key].replace(',','')

            courses.append(course_obj)
        
        already_loaded = json.load(open('devFiles/result2.json','r'))
        already_loaded.extend(courses)

        with open('devFiles/result2.json','w'):
            json.dump(already_loaded,open('devFiles/result2.json','a'),indent=2)


process = CrawlerProcess()
process.crawl(LetrotSpiderCoursesSpider)
process.start()