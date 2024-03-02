from pytube import YouTube
import sys

def videoDownload(linkReceived):
    try:
        videoObject = YouTube(linkReceived)
        video = videoObject.streams.get_highest_resolution()
        video.download()
    except:
        print("youtube link is invalid, there's an error.")


# This is meant to fetch data from the cmd
# use lenght of 2 to ensure that it doesn't take in the file name.
# length must be two.
if len(sys.argv) == 2: 
    linkToUse = sys.argv[1]
    videoDownload(linkToUse)
else:
    print("ensure you've typed in the link or provide a valid link")


    