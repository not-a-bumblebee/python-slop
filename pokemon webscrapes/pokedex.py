import os
import json
import datetime
import re
import string
import concurrent.futures

import requests

def getPokeObj(x):
    newDickt = {}
    item = x['pokemon_species']['name']
    number = x['entry_number']
    # url = x['pokemon_species']['url']

    getTypes = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(number)).json()

    types = []

    for k in getTypes['types']:
        types.append(k['type']['name'])

    # for z in getTypes['forms']:

    newDickt['name'] = item
    newDickt['national_id'] = number
    newDickt['type'] = types

    return newDickt

    # newArr.append(newDickt)

pokedexes = {0:'national',1:'kanto',2:'johto',3:'hoenn',4:'sinnoh',5:'unova'}


dadDickt={}

#Iterate through each dex
for j in range(1,7):
    res = requests.get('https://pokeapi.co/api/v2/pokedex/'+str(j))

    poke = res.json()


    newArr = []

    # iterate through all pokemon        // start multithreading here?
    with concurrent.futures.ThreadPoolExecutor() as executor:

        if(j - 1 == 0):
            results = executor.map(getPokeObj, poke['pokemon_entries'][:649])
        else:
            results = executor.map(getPokeObj, poke['pokemon_entries'])

        for g in results:
            newArr.append(g)

    dadDickt[pokedexes[j - 1]] = newArr
    print(dadDickt)



    # for i in poke['pokemon_entries'][:649]:
    #
    #     item = i['pokemon_species']['name']
    #     number =i['entry_number']
    #     # url = i['pokemon_species']['url']
    #
    #     #stops before gen 6
    #     if(number == 650):
    #         break
    #
    #     getTypes = requests.get('https://pokeapi.co/api/v2/pokemon/'+ str(number)).json()
    #
    #     types=[]
    #
    #     for k in getTypes['types']:
    #         types.append( k['type'])
    #
    #     # for z in getTypes['forms']:
    #
    #
    #     newDickt['name'] = item
    #     newDickt['national_id'] = number
    #     newDickt['type'] = types
    #
    #     newArr.append(newDickt)



with open('pokedex.json','w+') as file:
    json.dump(dadDickt,file)

