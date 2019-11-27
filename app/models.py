from . import db
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.dialects import postgresql
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Pitch(db.Model):
  '''
  maps to  pitch_collection table in database

  Args:
    db.Model: class from which sqlAlchemy properties are inherited
  '''

  __tablename__ = 'pitch_collection'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  body = db.Column(db.String(), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey('pitch_categories.id'), nullable=False)

  def is_body_more_than_150(self):
    return len(self.body) >= 150 if self.body is not None else False

# @classmethod
# def get_pitch_by_category(cls,category):
#     pitch = Pitch.query.filter_by(category = category)

#     return pitch

@classmethod
def get_user_pitch (cls,uname):
    pitch = Pitch.query.filter_by(user = uname ).all()

    return pitch
class PitchVote(db.Model):
  '''
  maps to pitch_votes table in database

  Args:
    db.Model: class from which sqlAlchemy properties are inherited
  '''

  __tablename__ = 'pitch_votes'
  id = db.Column(db.Integer, primary_key=True)
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitch_collection.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  vote_type = db.Column(postgresql.ENUM('upvote', 'downvote', name='vote_type', create_type='false'), nullable=False)

class PitchComment(db.Model):
  '''
  maps to pitch_comments table in database

  Args:
    db.Model: class from which sqlAlchemy properties are inherited
  '''

  __tablename__ = 'pitch_comments'
  id = db.Column(db.Integer, primary_key=True)
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitch_collection.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  comment = db.Column(db.String(), nullable=False)

# class Review(db.Model):
#     __tablename__ = 'reviews'
    
#     def save_review(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_reviews(cls,id):
#         reviews = Review.query.filter_by(movie_id=id).all()
#         return reviews    


