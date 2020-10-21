from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField 
from wtforms.validators import DataRequired, Length, ValidationError, Email


class EmailForm(FlaskForm):
    email = StringField('Enter email here:',
                validators=[DataRequired(), Email()])
    message = TextAreaField('Enter message:',
                validators=[DataRequired()])
    submit = SubmitField('Send Email')