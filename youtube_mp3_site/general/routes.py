from flask import render_template, Blueprint
# from youtube_mp3_site.download.utils import send_issue_email


general = Blueprint('general', __name__)

@general.route('/')
@general.route('/home')
def home():
    return render_template('home.html')

@general.route('/about')
def about():
    return render_template('about.html', title='About')

