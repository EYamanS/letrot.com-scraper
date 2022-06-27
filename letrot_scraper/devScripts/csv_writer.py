import json


JSON_FILENAME = 'result2-1'
CSV_FILENAME = 'courses'
data_to_write = json.load(open(f'devFiles/{JSON_FILENAME}.json','r'))


attrs = [
    'Nom',
    'Prix',
    'Distance',
    'Mode course',
    'Conditions',
    'Depart'
]


with open(f'results/{CSV_FILENAME}.csv','a') as fh:
    fh.write(','.join(attrs) + '\n')


for dic in data_to_write:
    with open(f'results/{CSV_FILENAME}.csv','a') as fh:
        fh.write(','.join([dic[attribute] for attribute in attrs]) + '\n')