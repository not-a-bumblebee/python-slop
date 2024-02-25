import os
import json
import datetime
import re


framePath = r"C:\Users\aznpa\Downloads\Clone High (2002) Season 1 S01 (480p AMZN.WEBDL x265 10bit AAC 2.0 EDGE2020)\Season 1\jpeggy"
getFrames = sorted(os.listdir(framePath))
getFrames.sort(key=lambda x:int(re.search(r"(?<=frame_)\d+", x).group()))
print("PATH IS:",getFrames[0])

pureArray = getFrames.copy()

with open("test.json", "r") as lib:
    cloneLib = json.load(lib)
    cloneLib = [x for x in cloneLib if x['episode']=='S01E01']

for i in getFrames:
