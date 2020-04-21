from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField, PasswordField, IntegerField, SubmitField,DateField,SelectField
from wtforms.validators import InputRequired,DataRequired

class DateForm(FlaskForm):
    username = StringField('Username', [InputRequired()])
    date    = DateField('Enter a date in YYYY-MM-DD format: ', [DataRequired()], format='%Y-%d-%m' )
    submit = SubmitField('Get Date')

