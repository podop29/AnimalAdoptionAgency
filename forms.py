from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField,  IntegerField, RadioField, SelectField

from wtforms.validators import InputRequired, URL, Optional

class AddPetForm(FlaskForm):
    'For adding pets to db'
    name = StringField("Pet Name", validators=[InputRequired(message="Must enter a pet name")])

    species =StringField("Species", validators=[InputRequired(message="Must enter your pets species")])

    photo_url = StringField("Img Url", validators=[Optional() ,URL()])

    age =  IntegerField("Age", validators=[Optional()])
     
    notes =  StringField("Extra Notes", validators=[Optional()])

    avalible = BooleanField("Available for adoption?")
