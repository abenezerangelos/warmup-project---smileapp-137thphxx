from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length, Email
from app.Model.models import User

class RegistrationForm(FlaskForm): 
	username = StringField('Username' ,validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password= PasswordField('Password',validators= [DataRequired()])
	password2 = PasswordField('Repeat Password', validators= [DataRequired(),EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self,username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('The username already exists! Please use a different username.')

    

