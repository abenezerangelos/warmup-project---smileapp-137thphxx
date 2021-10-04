from datetime import datetime
from app import db
#from sqlalchemy import postTags
#from sqlalchemy.orm import relationship
 
postTags = db.Table('postTags',
         db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
         db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
         )

class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    body = db.Column(db.String(1500))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    likes = db.Column(db.Integer, default = 0)
    happiness_level = db.Column(db.Integer, default = 3)


    tags = db.relationship('Tag', secondary = postTags, primaryjoin=(postTags.c.post_id == id), backref=db.backref('postTags', lazy='dynamic'), lazy='dynamic')


    def get_tags(self):
        return self.tags


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(20))

    def __repr__(self):
        rep = 'Person(' + str(self.id) + ',' + self.name + ')'
        return rep