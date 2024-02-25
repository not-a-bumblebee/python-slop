import os
import json



PATH = r"C:\Users\aznpa\Downloads\Clone High (2002) Season 1 S01 (480p AMZN.WEBDL x265 10bit AAC 2.0 EDGE2020)\Season 1\subs"
getFiles = sorted(os.listdir(PATH))
print("PATH IS:",getFiles)

jason = []


for z in getFiles:



    with open(PATH + "\\" + z,mode="r",encoding='utf-8-sig') as file:
        #everything means the whole episode
        everything=file.read().strip().split("\n\n")

        print(len(everything))
        for i in everything:


            test = i.split("\n")

            dickt = {}
            dickt["episode"] = z[20:26]
            dickt["id"] = test[0]
            dickt["lines"] = " ".join(test[2:])

            timeStamp = test[1].split("-->")

            dickt["startTime"] = timeStamp[0].strip()
            dickt["endTime"] = timeStamp[1].strip()
            dickt["frame"]
            print("DICKT:",dickt)
            print(test)

            jason.append(dickt)

with open("test.json", "w") as file:
    file.write(json.dumps(jason))
