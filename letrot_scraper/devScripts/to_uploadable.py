import json

with open('devFiles/result2-1.json','r') as fh:
    gathered_courses = json.load(fh)
    print(gathered_courses)
    for obj in gathered_courses:
        obj.pop('course_link')

with open('results/courses.json','w') as fh:
    json.dump(gathered_courses,fh,indent=3)