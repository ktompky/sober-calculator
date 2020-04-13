from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class DateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    date    = IntegerField('Enter a date in YYYY-MM-DD format: ', validators= [DataRequired()])
    submit = SubmitField('Get Date')