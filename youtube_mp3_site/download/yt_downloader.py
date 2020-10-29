from youtube_mp3_site.config import Config as cfg
from youtube_mp3_site.download.utils import FileRenaming as file_rename
from youtube_mp3_site.download.utils import Cookies
import youtube_dl
import os

video_path = os.path.abspath(cfg.PATH_TO)
SLEEP_TIME = 30

class YoutubeDownloader:
    def __init__(self, url, is_mp3=False):
        self.url = url
        # Dictates whether to download mp3 or not.
        self.is_mp3 = is_mp3
        # YoutubeDL options                    
        self.options = {
            'outtmpl': cfg.PATH_TO + '\\%(id)s.%(ext)s',
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'sleep_interval': SLEEP_TIME,
            'cookies': Cookies.create_cookie()
        }
        # update more options if mp3
        if is_mp3:
            self.options.update(
                {
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],

                    'keepvideo': False,
                    'format': 'bestaudio/best'

                }
            )

        # YoutubeDL object
        self.ydl = youtube_dl.YoutubeDL(self.options)        
        # Info extracted from video, and downloads file
        self.info_dict = self.ydl.extract_info(url, download=True)
        # Title of video
        self.video_title = self.info_dict.get("title", None)
        # ID of video
        self.video_id = self.info_dict.get("id", None)
        # Replace unacceptable characters from video title
        self.new_title = "".join(file_rename.FILE_REPLACE_CHARS.get(c,c) for c in self.video_title)
        # Title if file is an mp3
        self.mp3_title = f'{self.video_id}.mp3'
        # Title if file is an mp4
        self.mp4_title = f'{self.video_id}.mp4'        

    

    @property
    def get_audio_clip(self):
        return self.mp3_title

    @property
    def get_video_clip(self):
        return self.mp4_title
    


