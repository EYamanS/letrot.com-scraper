from typing import Counter
import scrapy
import json
import requests
import time

class LetrotSpiderCoursesSpider(scrapy.Spider):
    name = 'letrot_spider_courses'
    allowed_domains = ['www.letrot.com']
    start_urls = ["https://www.letrot.com/"+json.loads(line)["href"]+'/json' for line in open('devFiles/result1.json','r')]
    counter = 0
    attrs = ['Nom','Prix',"Distance","Mode course","Conditions","Depart"]

    def parse(self, response):

        courses = []

        responseObj = json.loads(response.text)
        course_responses = [course for course in responseObj['course']]
    
        for course_response in course_responses:

            course_obj = {
                'Nom':'C'+str(course_response['numCourse']),
                'Prix': str(course_response['allocation']) + 'E',
                'Distance': str(course_response['distance']+'m'),
                'Mode course': str(course_response['discipline']),
                'Conditions': str(course_response['conditionsEngagement']).replace('<br />',' '),
                'course_link': str(course_response['linkPrix']),
                'Depart': 'Volt' if 'autostart' not in str(course_response['conditionsEngagement']) else 'Autostart'
            }


            for key in course_obj:
                if ',' in course_obj[key]:
                    course_obj[key] = course_obj[key].replace(',','')

            courses.append(course_obj)
        
        already_loaded = json.load(open('devFiles/result2.json','r'))
        already_loaded.extend(courses)

        with open('devFiles/result2.json','w'):
            json.dump(already_loaded,open('devFiles/result2.json','a'),indent=2)
