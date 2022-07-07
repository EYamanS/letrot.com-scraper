import json


JSON_FILENAME = 'result2-1'
CSV_FILENAME = 'Course'
data_to_write = json.load(open(f'devFiles/{JSON_FILENAME}.json','r'))


with open(f'results/{CSV_FILENAME}.csv','w') as fh:
    fh.write('')

attrs = [
    'nom-course',
    'prix-course',
    'distance-course',
    'condition-course',
    'mode-course',
    'depart-course',
]


with open(f'results/{CSV_FILENAME}.csv','a') as fh:
    fh.write(','.join(attrs) + '\n')


for dic in data_to_write:
    with open(f'results/{CSV_FILENAME}.csv','a') as fh:
        fh.write(','.join([dic[attribute] for attribute in attrs]) + '\n')