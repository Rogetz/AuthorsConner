from pytube import YouTube


def videoDownload(linkReceived):
    try:
        videoObject = Youtube(linkReceived)
        video = videoObject.streams.get_highest_resolution()
        video.download()
    except:
        print("youtube link is invalid, there's an error.")
