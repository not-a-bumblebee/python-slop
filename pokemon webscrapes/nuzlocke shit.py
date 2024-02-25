import os
import json
import datetime
import re
import string

import requests

def search(x):
    reg = re.search(r"(?<=oute )\d+", x)
    # print(reg)
    if reg != None:
        return int(reg.group())
    else:
        return 9999

generations = {1:'kanto',2:'johto',3:'hoenn',4:'sinnoh',5:'unova'}
newDickt = {}
for j in range(1,6):
    res = requests.get('https://pokeapi.co/api/v2/region/'+str(j))

    locations = res.json()

    newArr = []
    for i in locations['locations']:
        item = i['name']
        if generations[j] in i['name']:
            item = item.replace(generations[j],'')

        item=item.replace('-',' ')


        newArr.append(string.capwords(item.strip()) )

    newArr.sort(key=search)

    print(newArr)
    newDickt[generations[j]] = newArr

with open('routes.json','w+') as file:
    json.dump(newDickt,file)

