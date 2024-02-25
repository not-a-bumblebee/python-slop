import os
import json
import datetime
import re


framePath = r"C:\Users\aznpa\Downloads\Clone High (2002) Season 1 S01 (480p AMZN.WEBDL x265 10bit AAC 2.0 EDGE2020)\Season 1\jpeggy"
getFrames = sorted(os.listdir(framePath))
getFrames.sort(key=lambda x:int(re.search(r"(?<=frame_)\d+", x).group()))
print("PATH IS:",getFrames)

with open("ep1 frames final.json", 'w') as file:
    file.write(json.dumps(getFrames))