import urllib
import json
from bs4 import BeautifulSoup

with urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_time_zone_abbreviations') as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', attrs={ "class" : "wikitable"})

headers = [header.text for header in table.find_all('th')]

rows=[]
i=0
jsonn={}

for row in table.find_all('tr'):
    vall=[]
    for val in row.find_all('td'):
        vall.append(val.text)    
    rows.append(vall)
rows.pop(0) 

for var in rows:
    mydict={}
    mydict['place']=var[1]
    mydict['offset']=var[2]
    jsonn[var[0]]=mydict

print(jsonn)

with open('timezone.txt', 'w',encoding='utf8') as outfile:
     json.dump(jsonn, outfile, sort_keys = True, indent = 4,ensure_ascii = False)