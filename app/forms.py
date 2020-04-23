from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import InputRequired,DataRequired
from wtforms.fields.html5 import DateField

class DateForm(FlaskForm):
    username = StringField('Enter your first name: ', [InputRequired()])
    date    = DateField('Enter you first date of sobriety: ', [DataRequired()], format='%Y-%d-%m' )
    submit = SubmitField('Get Date')

 