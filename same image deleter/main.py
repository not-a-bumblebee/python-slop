from PIL import Image, ImageChops
import os

# Resets the test
os.system('xcopy /s /y "./before" "./after"')


# picDir = input("Enter the directory: ")
picDir = './after'

arr = os.listdir(picDir)
print(arr)
# THIS IS THE ARRAY OF ITEMS TO DELETE
hit = []
count = 1
for i in arr:
    first = Image.open(picDir+'/'+i)
    for g in range(count,len(arr)):

        print("loop" + str(count))
        second = Image.open(picDir+'/'+ arr[g])
        diff = ImageChops.difference(first.convert('RGB'),second.convert('RGB'))
        if not diff.getbbox():
            print(diff.getbbox())
            if arr[g] not in hit:
                hit.append(arr[g])
            print(arr[g])
        second.close()
    first.close()



    count +=1



print("things to wack",hit)
for z in hit:
    cumzone = picDir + "\\"+ z
    print(cumzone)
    os.remove(cumzone)


#img = Image.open("twitterclone.jpg")
#img2 = Image.open("twitter.jpg")

#diff = ImageChops.difference(img,img2)

#print(diff.getbbox())
#if diff.getbbox():
#    diff.show()