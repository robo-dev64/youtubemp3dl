from local_packages.YouPy.youtube_item import YouTubeItem
# from YouPy import YouTubeItem
from moviepy.editor import VideoFileClip, AudioClip
from youtube_mp3_site.config import Config as cfg
from youtube_mp3_site.download.utils import FileRenaming as file_rename
from youtube_mp3_site.download.utils import Cookies as cookie



class YoutubeDownloader:
    def __init__(self, url, is_mp3=False):
        self.url = url        
        self.youtube_video = YouTubeItem(url=self.url, request_headers={'cookie': cookie.create_cookie()})
        self.video_title = self.youtube_video.title
        # replace any flagged characters to prevent OSError
        self.mp3_title = f'{"".join(file_rename.FILE_REPLACE_CHARS.get(c, c) for c in self.video_title)}.mp3'
        print(self.mp3_title)
        self.video_clip = None
        self.is_mp3 = is_mp3
    
    def download_mp3(self):
        self.download_mp4()
        self.audio_clip = self.video_clip.audio
        self.audio_clip.write_audiofile("%s\\%s" % (cfg.PATH_TO, self.mp3_title))
        self.audio_clip.close()
        self.video_clip.close() 

    def download_mp4(self):
        self.video = self.youtube_video.streams.filter(progressive=True, file_extension='mp4').first().download(cfg.PATH_TO)
        self.video_clip = VideoFileClip(self.video)    
        if not self.is_mp3:
            self.video_clip.close()    

    @property
    def get_audio_clip(self):
        return self.mp3_title

    @property
    def get_video_clip(self):
        return self.video_clip.filename
    


