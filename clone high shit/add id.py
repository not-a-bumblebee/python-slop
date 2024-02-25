#RENAMES ALL IMAGES TO INCLUDE THE ID OF THE SUBTITLE TO ASSOCIATE EACH FRAME WITH.
import os
import json

#path to a folder full of images
PATH =r"C:\Users\aznpa\Downloads\Clone High (2002) Season 1 S01 (480p AMZN.WEBDL x265 10bit AAC 2.0 EDGE2020)\Season 1\ep1 frames"
getFiles = sorted(os.listdir(PATH))
print("PATH IS:",getFiles)

with open('ep1only.json') as file:
    cloneLib = json.load(file)
    cloneLib = [x for x in cloneLib if x['episode'] == 'S01E01']

#iterate through each json in the arr and add the sub id to each name,while removing their items from another array
#then iterate through that other array and give them a sub_00
for n,i in enumerate(cloneLib):
    for k in i["frames"]:
        old = PATH+"\\"+k
        new = PATH+"\\" + k[:-5] + "_sub_" + i["id"]+".webp"
        os.rename(old,new)
        getFiles.remove(k)

for j in getFiles:
    old = PATH + "\\" + j
    new = PATH + "\\" + j[:-5] + "_sub_" + "00" + ".webp"
    os.rename(old, new)


