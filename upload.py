import requests
import datetime


API_KEY = '1928c06e65c60106bb1705ab681af810'

x = requests.post(f'https://letrotfrancais.bubbleapps.io/version-test/api/1.1/wf/nouvelle-course?APIKey={API_KEY}',{
    "nom-reunion": "EREGLI 01/07/22", 
    "nom-hippodrome": "EREGLI", 
    "date-reunion": datetime.datetime(2022,7,1),
    "nom-course": "EREGLI 01/07/22 C2",
    "prix-course": "24 000E",
    "distance-course": "3 675m",
    "mode-course": "Attele",
    "condition-course": "Pour chevaux entiers et hongres de 5 ans n'ayant pas gagne 50.000. - Recul de 25 m. a  25.000.",
    "depart-course": "Volte",
    'numero-concurrent':2,
    "cheval-concurrent":'HASTINGS INDIEN',
    'jockey-concurrent':'E. LAMBERTZ',
    'entraineur-concurrent':'E. LAMBERTZ',
    'distance-concurrent':'2 950',
    'gain-concurrent':5830,
    'nom-concurrent':'1-HASTINGS INDIEN-EREGLI 01/07/22 C2'})
#requests.Response.
print(x.content)