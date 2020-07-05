from pytube import *

#Give The Video Link

url = "........copy the video link.........."

path_to_save_video = "........enter the path where you want to save the video..........."

obj = YouTube(url)

# strms = obj.streams.all()
# for s in strms:
#     print(s)

#first streams is always a high resolution file

strm = obj.streams.first()

print(strm.filesize)

print(strm.title)

print(obj.description)

strm.download(path_to_save_video)
print("done....")

