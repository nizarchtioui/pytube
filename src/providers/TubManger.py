from pytube import YouTube
import time, sys
from pydub import AudioSegment


class YoutubeManager:
    def __init__(self):
        pass
    @staticmethod
    def DownloadVideo(url,subtyp):
        try:
            id_video = url.split("v=")[1]
            yt = YouTube(url)
            
            subtyp = subtyp.lower()
           
            if subtyp == "mp3":
                streams = yt.streams.filter(subtype='mp4').first()
                r = streams.download(r"static/db")
                track = AudioSegment.from_file(r)
                print('CONVERTING')
                track.export(r"static/db/%s.mp3"%id_video, format='mp3')
                return r"static/db/%s.mp3"%id_video
            else:
                streams = yt.streams.filter(subtype=subtyp).first()
                r = streams.download(r"static/db")
           
            return r
        except:
            print(sys.exc_info())
            return False
     