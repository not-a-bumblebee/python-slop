import json
import cloudinary
import cloudinary.uploader
import cloudinary.api
import concurrent.futures
cloudinary.config(
    cloud_name = "no",
    api_key = "no",
    api_secret = "no"
)
with open('ep1 frames final.json', 'r') as file:
    frameList = json.load(file)

size = len(frameList)


def upload(frame):
    try:
        cloudinary.uploader.upload_image(r"C:\Users\aznpa\Downloads\Clone High (2002) Season 1 S01 (480p AMZN.WEBDL x265 10bit AAC 2.0 EDGE2020)\Season 1\jpeggy\\"+frame,
                use_filename = True,
                unique_filename = False,
                resource_type = "image",
                folder = "clone high/ep1")
        return frame + " uploaded"

    except:
        return frame + " ERROR"



with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(upload,frameList)

    for n,i in enumerate(results):
        print(str(n) + " of " + str(size) + ";" +i)



#
# for n,i in enumerate(frameList):
#
#
#     cloudinary.uploader.upload_image(r"C:\Users\aznpa\Downloads\Clone High (2002) Season 1 S01 (480p AMZN.WEBDL x265 10bit AAC 2.0 EDGE2020)\Season 1\jpeggy\\"+i,
#         use_filename = True,
#         unique_filename = False,
#         resource_type = "image",
#         folder = "clone high/ep1")
#
#     print(str(n) + " of " + str(size) + " for " +i)