import json

with open("routes.json",'r') as file:
    routes = json.load(file)

print(routes['unova'])

newArr =[]

for n,i in enumerate(routes['johto']):

    newArr.append({"name":i,'status':0})

print(newArr)

with open('save template hgss.json','w') as file:
    json.dump(newArr,file)




