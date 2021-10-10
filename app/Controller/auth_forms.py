from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length, Email
from app.Model.models import User
from flask_login import current_user

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

    
class LoginForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired()])
	password = PasswordField('Password',validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit=SubmitField('Sign In')
