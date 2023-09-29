import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100))
    email = Column(String(100))
    biography = Column(String(250))
    posts = relationship('Post', back_populates='user')
    

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    image_url = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='posts')

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    user = relationship('User', back_populates='comments')

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    followed_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    follower = relationship('User', foreign_keys=[follower_id], back_populates='following')
    followed_by = relationship('User', foreign_keys=[followed_id], back_populates='followers')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
