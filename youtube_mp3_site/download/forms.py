from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, URL, ValidationError
import re


class YoutubeForm(FlaskForm):
    video = StringField('Enter valid Youtube video URL here:', 
                        validators=[DataRequired()])
    mp3_submit = SubmitField('Get MP3')
    video_submit = SubmitField('Get MP4')
    
    
    def validate_video(self, url):

        regex = (      
            r"[\[https*://\]*www\.]*"
            r"youtube.com\/watch\?v="
            r"[a-zA-Z0-9-._]{11}(?!&list=)"
            # r"(&list=[a-zA-Z0-9-._]{34}"
            # r"&index=[0-9]{1,4})*"
        )

        if not re.search(regex, str(url.data)):
            raise ValidationError("Invalid Youtube URL provided.")
    