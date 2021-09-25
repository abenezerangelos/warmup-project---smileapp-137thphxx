from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import  DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput

from app.Model.models import Post, Tag

def get_tags():
     return Tag.query.all()

def get_tagslabel(thePost):
     return thePost.name



class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    happiness_level = SelectField('Happiness Level',choices = [(3, 'I can\'t stop smiling'), (2, 'Really happy'), (1,'Happy')])
    tag =  QuerySelectMultipleField( 'Tag', query_factory=get_tags , get_label=get_tagslabel, widget=ListWidget(prefix_label=False), 
      option_widget=CheckboxInput() )
    submit = SubmitField('Post')
    body = TextAreaField('Body', validators=[Length(min=0, max=1500)])

class SortForm(FlaskForm):
    Choices = SelectField(choices = [(4,'Happiness level'),(3,'Date'), (2, 'Title'), (1,'of likes')])
    Submit = SubmitField('Refresh')
