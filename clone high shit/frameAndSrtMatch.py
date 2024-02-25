import os
import json
import datetime
import re

def filterFunction(x, start,end):

    # frameNumber =  x.split("_")[-1][:-5]
    #convert the frame number to seconds, then into a date time object.
    frameToSec = int(re.search(r"(?<=frame_)\d+", x).group()) / 30
    frameDelta = datetime.timedelta(seconds=frameToSec)

    # a = str(frameDelta)[:6]
    # print("filter:",a)
    # str(time)[:8] in str(frameDelta)

    if(frameDelta>= start and frameDelta<=end):
        return True

    return False


framePath = r"C:\Users\aznpa\Downloads\Clone High (2002) Season 1 S01 (480p AMZN.WEBDL x265 10bit AAC 2.0 EDGE2020)\Season 1\jpeggy"
getFrames = sorted(os.listdir(framePath))
getFrames.sort(key=lambda x:int(re.search(r"(?<=frame_)\d+", x).group()))
print("PATH IS:",getFrames[0])

pureArray = getFrames.copy()

with open("test.json", "r") as lib:
    cloneLib = json.load(lib)
    cloneLib = [x for x in cloneLib if x['episode']=='S01E01']


#enumerates over the search index json for the specific episode
for n,i in enumerate(cloneLib):
    print("Json:",i)




    #start and end duration of the subtitle
    startTime =i['startTime']
    endTime =i['endTime']

    print("Start time:",startTime)

    #converts the start and end duration into a date time object.
    startTime = startTime.replace(",",".").strip()
    endTime = endTime.replace(",",".").strip()
    print(startTime)
    startTime = datetime.datetime.strptime(startTime,"%H:%M:%S.%f")
    startTime = datetime.timedelta(hours=startTime.hour, minutes=startTime.minute, seconds=startTime.second, microseconds=startTime.microsecond)
    endTime = datetime.datetime.strptime(endTime,"%H:%M:%S.%f")
    endTime = datetime.timedelta(hours=endTime.hour, minutes=endTime.minute, seconds=endTime.second, microseconds=endTime.microsecond)
    print("start time:",startTime)
    print("end time:",endTime)




    #returns an array with frames that fit the time span for the subtitle.
    # filteredShit = list(filter(lambda x:filterFunction(x,startTime,endTime),getFrames))

    renameStack =[]
    validStack = []

    for z in getFrames:
        frameToSec = int(re.search(r"(?<=frame_)\d+", z).group()) / 30
        frameDelta = datetime.timedelta(seconds=frameToSec)

        # a = str(frameDelta)[:6]
        # print("filter:",a)
        # str(time)[:8] in str(frameDelta)

        if(frameDelta <startTime):
            renameStack.append(z)
            # validStack.append(z)
            old = framePath + "\\" + z
            new = framePath + "\\" + z[:-4] + "_sub_" + "00" + ".jpg"
            # os.rename(old, new)

        elif (frameDelta >= startTime and frameDelta <= endTime):
            renameStack.append(z)


            old = framePath + "\\" + z
            new = framePath + "\\" + z[:-4] + "_sub_" + i['id'] + ".jpg"
            # os.rename(old, new)
            validStack.append(z)
        else:
            break


    # print("Filtered Items:",len(filteredShit))

    # for z in filteredShit:
    #     getFrames.remove(z)

    for z in renameStack:
        getFrames.remove(z)

    output = []

    # changed to only use the first frame
    cloneLib[n]['startingFrame']=validStack[0]

    cloneLib[n]['startingIndex'] = pureArray.index(validStack[0])



    # print(filteredShit)
    # for i in filteredShit:
    #     frameNumber = i.split("_")[-1][:-5]
    #     frameToSec = int(frameNumber) / 30
    #     frameDelta = (datetime.timedelta(seconds=frameToSec))
    #     output.append([i,str(frameDelta)])



    # print("Possible matches for ",startTime,"and ",endTime,": ",output)


    # with open('data.txt','a') as file:
    #     file.write(str(output))
if(len(getFrames) >0):
    for i in getFrames:
        old = framePath + "\\" + i
        new = framePath + "\\" + i[:-4] + "_sub_" + "00" + ".jpg"
        # os.rename(old, new)
with open('ep1onlybeta.json', 'w') as file:
    file.write(json.dumps(cloneLib))