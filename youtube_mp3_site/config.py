import os

class Config:    
    SECRET_KEY = os.environ.get('SECRET_KEY')     
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    PATH_TO = 'youtube_mp3_site\\static\\output'
    static_folder = "static\\output"