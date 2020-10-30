from flask import render_template, Blueprint
from youtube_dl.utils import DownloadError as dl_error

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(dl_error)
def error_download(error):
    return render_template('errors/download_error.html', errors=[error.exc_info])

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500
