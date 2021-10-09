from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from flask_sqlalchemy import sqlalchemy
from config import Config
from app.Controller.auth_forms import RegistrationForm
from app.Model.models import User

from app import db

bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER 

@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
	rform = RegistrationForm()
	if rform.validate_on_submit():
		user = User(username= rform.username.data, email=rform.email.data, password_hash = rform.password_hash.data)
		user.set_password(rform.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('routes.index'))
	return render_template('register.html', form =rform)
