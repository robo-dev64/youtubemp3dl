from flask import render_template, Blueprint, redirect, flash, send_file, send_from_directory, url_for
from youtube_mp3_site.contact.forms import EmailForm
from flask import request
from youtube_mp3_site.contact.utils import send_issue_email



contact = Blueprint('contact', __name__)

@contact.route('/contact', methods=['GET', 'POST'])
def send_contact():
    form = EmailForm()
    if form.validate_on_submit():
        send_issue_email(user=form.email, body=form.message)
        flash('Email successfully sent.', 'success')
    return render_template('contact.html', title='Contact', form=form)