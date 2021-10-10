from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from flask_sqlalchemy import sqlalchemy
from config import Config
from app.Controller.auth_forms import RegistrationForm, LoginForm
from app.Model.models import User
from flask_login import current_user, login_user, logout_user, login_required


from app import db


bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER 

@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
	rform = RegistrationForm()
	if rform.validate_on_submit():
		user = User(username= rform.username.data, email=rform.email.data)
		user.set_password(rform.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('routes.index'))
	return render_template('register.html', form =rform)

@bp_auth.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    lform = LoginForm()
    if lform.validate_on_submit():
        user= User.query.filter_by(username =lform.username.data).first()

        if(user is None) or (user.check_password(lform.password.data) == False):
            flash('Invalid-username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember = User.query.filter_by(username =lform.remember_me.data).first())
        return redirect(url_for('routes.index'))
    return render_template('login.html',title='Sign In',form=lform)
    
@bp_auth.route('/logout',methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))