#import the package
from pytube import YouTube

url = 'https://www.youtube.com/watch?v=dsGODTySH0E'
my_video = YouTube(url)

print("*********************Video Title************************")
#get Video Title
print(my_video.title)

print("********************Downloading video*************************")
#set stream resolution
my_video = my_video.streams.get_highest_resolution()

#Download video
my_video.download()
