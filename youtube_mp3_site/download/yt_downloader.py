from moviepy.editor import VideoFileClip, AudioClip
from youtube_mp3_site.config import Config as cfg
from youtube_mp3_site.download.utils import FileRenaming as file_rename
from youtube_mp3_site.download.utils import Cookies as cookie
import youtube_dl
import os


class YoutubeDownloader:
    def __init__(self, url, is_mp3=False):                      
        self.options = {
            'outtmpl': cfg.PATH_TO + '\\%(id)s.%(ext)s',
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        }

        self.ydl = youtube_dl.YoutubeDL(self.options)

        self.info_dict = self.ydl.extract_info(url, download=True)
        self.video_title = self.info_dict.get("title", None)
        self.video_id = self.info_dict.get("id", None)
        # replace any flagged characters to prevent OSError
        self.new_title = "".join(file_rename.FILE_REPLACE_CHARS.get(c,c) for c in self.video_title)
        self.mp3_title = f'{self.video_id}.mp3'
        self.mp4_title = f'{self.video_id}.mp4'
        self.video_clip = None
        self.is_mp3 = is_mp3
    
    def download_mp3(self):
        self.download_mp4()
        self.audio_clip = self.video_clip.audio
        self.audio_clip.write_audiofile("%s\\%s" % (cfg.PATH_TO, self.mp3_title))
        self.audio_clip.close()
        self.video_clip.close() 

    def download_mp4(self):        
        self.video_clip = VideoFileClip("%s\\%s" % (cfg.PATH_TO, self.mp4_title))    
        if not self.is_mp3:
            self.video_clip.close()

    @property
    def get_audio_clip(self):
        return self.mp3_title

    @property
    def get_video_clip(self):
        return self.video_clip.filename
    


