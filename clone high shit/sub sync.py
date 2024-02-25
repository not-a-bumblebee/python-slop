import os
import json
import datetime

def subSync(range,delta=0):
    if (delta == 0):
        return range
    range= range.replace(",",".")
    output = range.split("-->")


    tempStart= output[0].split(":")
    tempEnd = output[1].split(":")
    newStart= datetime.timedelta(minutes=int(tempStart[1]),seconds=float(tempStart[2])) + datetime.timedelta(seconds=delta)
    newEnd = datetime.timedelta(minutes=int(tempEnd[1]),seconds=float(tempEnd[2])) + datetime.timedelta(seconds=delta)

    if(newStart <= datetime.timedelta(seconds=0)):
        return "time error"


    output[0]= str(newStart)[0:-3]
    output[1] = str(newEnd)[0:-3]

    output= " --> ".join(output)

    return output.replace(".",",")



PATH = r"C:\Users\aznpa\Desktop\clone high subtitles"
getFiles = sorted(os.listdir(PATH))
print("PATH IS:",getFiles)

jason = []


# for i in getFiles:
#


with open(PATH + "\\" + getFiles[1],mode="r",encoding='utf-8-sig') as file:
    #everything means the whole episode
    everything=file.read().strip().split("\n\n")
    print(everything)

    for i in everything:

        test = i.split("\n")
        print(test)
        test[1] = subSync(test[1],-2)

        jason.append("\n".join(test))
        jason.append("\n")


with open("test.srt", "w", encoding='utf-8-sig') as file:
    file.write("\n".join(jason))
