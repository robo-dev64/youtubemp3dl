from flask import render_template, Blueprint, redirect, flash, send_file, send_from_directory, url_for, safe_join, request, Response
from youtube_mp3_site.download.forms import YoutubeForm
from youtube_mp3_site.download.yt_downloader import YoutubeDownloader
from youtube_mp3_site.config import Config as cfg
import io
import os

download = Blueprint('download', __name__)


@download.route('/download', methods=['GET', 'POST'])
def download_mp3():

    form = YoutubeForm()

    if form.validate_on_submit():        
        
        # Create YoutubeDownloader object
        video = YoutubeDownloader(str(form.video.data), form.mp3_submit.data)
        
        if form.mp3_submit.data:

            audio_clip_ret_data = io.BytesIO()

            with open(os.path.abspath("%s\\%s" % (cfg.PATH_TO, str(video.get_audio_clip))), 'rb') as fo:
                audio_clip_ret_data.write(fo.read())

            audio_clip_ret_data.seek(0)
            
            # remove files from path
            os.remove(os.path.abspath("%s\\%s" % (cfg.PATH_TO, str(video.get_audio_clip))))

            # send file
            return send_file(audio_clip_ret_data, 
                                as_attachment=True, 
                                attachment_filename=f'{video.new_title}.mp3',
                                mimetype='application/mp3')

        else:

            video_clip_ret_data = io.BytesIO()

            with open(os.path.abspath("%s\\%s" % (cfg.PATH_TO, str(video.get_video_clip))), 'rb') as fo:
                video_clip_ret_data.write(fo.read())
            video_clip_ret_data.seek(0)

            # remove files from path
            os.remove(os.path.abspath("%s\\%s" % (cfg.PATH_TO, str(video.get_video_clip))))

            return send_file(video_clip_ret_data, 
                                as_attachment=True,
                                attachment_filename=f'{video.new_title}.mp4',
                                mimetype='application/mp4')



    return render_template('download.html', title='Download', form=form)
