from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from config import Config

from app import db
from app.Model.models import Post
from app.Controller.forms import PostForm

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


@bp_routes.route('/', methods=['GET','POST'])
@bp_routes.route('/index', methods=['GET','POST'])
def index():
    posts = Post.query.order_by(Post.timestamp.desc())
    return render_template('index.html', title="Smile Portal", posts=posts.all())

@bp_routes.route('/postsmile', methods=['GET','POST'])
def postsmile():
    pForm = PostForm()
    if pForm.validate_on_submit():
        newpForm = Post(title= pForm.title.data, body=pForm.body.data, timestamp=pForm.timestamp.data, likes=pForm.likes.data, happiness_level=pForm.happiness_level.data)
        db.session.add(newpForm)
        db.session.commit()
        flash('Congratulations, you are now post new smile!')
        return redirect(url_for('postsmile'))
    return render_template('create.html',form = pForm)

@bp_routes.route('/like/<post_id>', methods=['POST'])