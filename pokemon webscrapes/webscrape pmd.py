import os
import json
import re
import string
import time

from selenium import  webdriver

import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36';"}
# webdriver = webdriver.Firefox()
# webdriver.get('https://gamefaqs.gamespot.com/ds/955859-pokemon-mystery-dungeon-explorers-of-sky/faqs/58014')
# time.sleep(2)
page= requests.get('https://gamefaqs.gamespot.com/ds/955859-pokemon-mystery-dungeon-explorers-of-sky/faqs/58014',headers=headers, timeout=(10.05,270))
soup = BeautifulSoup(page.content,'html.parser')
table = soup.find_all('table')[3]
# print(page.json())
print(len(table.find_all('tr')))
arr = []
for i in table.find_all('tr'):


    dickt = {}
    # print(i.td)
    if(i.td):
        dickt['question'] = i.td.text
        dickt['answers'] = []

        for k in i.find_all('th'):
            answer = re.split(r' (?=\()',k.text)
            text = answer[0]
            print(text)
            effect =re.split(r', and|,|and',answer[1][1:-1])
            effects =[]

            for z in effect:
                z = z.strip()
                z= z.split(' ')
                z[1] = int(z[1])
                effects.append(z)

            dickt['answers'].append([text,effects])


        arr.append(dickt)

print(arr)

with open('testx.json','w+') as file:
    json.dump(arr,file)