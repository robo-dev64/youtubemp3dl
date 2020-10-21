from flask import Flask
from flask_mail import Mail
from youtube_mp3_site.config import Config

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)

    from youtube_mp3_site.errors.error_handlers import errors
    from youtube_mp3_site.general.routes import general
    from youtube_mp3_site.contact.routes import contact
    from youtube_mp3_site.download.routes import download
        
    app.register_blueprint(errors)
    app.register_blueprint(general)
    app.register_blueprint(contact)
    app.register_blueprint(download)
    

    return app