import os
import json
import datetime
import re
import string
import concurrent.futures

import requests
from bs4 import BeautifulSoup

#HG/SS REGIONAL DEX
page= requests.get('https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_Unova_Pok%C3%A9dex_number_(Black_2_and_White_2)#.23252_-_.23300_Sneasel_-_Genesect')
soup = BeautifulSoup(page.content,'html.parser')
mons= soup.find_all('tbody')[:7]
# print(mons[0].find('a'))
arr = []

for i in mons:
    for k in i.find_all('tr')[1:]:

        dickt={}
        local_dex = int(k.find_all('td')[0].text[1:].strip())
        nat_dex =  int(k.find_all('td')[1].text[1:].strip())

        name = k.find('a')['title'].strip()

        type=[]
        for j in k.find_all('span'):
            type.append(j.text.strip())

        dickt['name'] = name
        dickt['national_id'] = nat_dex
        dickt['local_id'] = local_dex
        dickt['type'] = type

        arr.append(dickt)


# print(mons[0],"\n\n",mons[11],mons[0].find('a').text.strip(),"\n",mons[0].find_all('td')[0].text.strip(),mons[0].find_all('td')[1].text.strip())

print(arr)

with open('bw2dex.json','w+') as file:
    json.dump(arr,file)