import os
import datetime

getDir = r"C:\Users\aznpa\Downloads\Clone High (2003) Season 1 S01 + Extras (480p DVD x265 HEVC 10bit AAC 2.0 r00t)\ep1_noref"

getFiles = sorted(os.listdir(getDir))

print(getFiles[6][21:-5])

def frameToTime(a):
    print("Initially",a," seconds")
    seconds = round(a/30,1)
    print("Seconds:",seconds)
    seconds = str(seconds).split(".")
    time = str(datetime.timedelta(seconds=int(seconds[0]))) + ":" + seconds[1]
    return time.replace(":","-")    

print("Files here:",getFiles)
newFileNames={}
frameToTime(round(float(getFiles[6][21:-5]),2))

for v in getFiles:
    fileName = v[:-5]
    frame = v[21:-5]
    time = frameToTime(int(frame))
    time.replace(":","-")

    newFileNames[v]=fileName+"_"+time+".webp"

print("Dickt",newFileNames)
input("Is everything ok?")

for i in newFileNames:
    oldPath = getDir + "\\" + i
    newPath = getDir + "\\" +newFileNames[i]
    os.rename(oldPath,newPath)


# # os.remove()