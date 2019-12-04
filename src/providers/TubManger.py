from pytube import YouTube
import time, sys

class YoutubeManager:
    def __init__(self):
        pass
    @staticmethod
    def DownloadVideo(url,subtyp):
        try:
            yt = YouTube(url)
            subtyp = subtyp.lower()
            streams = yt.streams.filter(subtype=subtyp).first()
            print(streams)
            r = streams.download(r"static/db")
           
            return r
        except:
            print(sys.exc_info())
            return False
     