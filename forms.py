from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField

class ContactForm(FlaskForm):
    name = TextField("Name")
    email = TextField("Email")
    message = TextField("Message")
    submit = SubmitField("Send")
