from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property
#user_id field is defined as a ForeignKey that references the users table
#we also add created_at and updated_at fields that use Python's built-in datetime module to generate the timestamps
class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  vote_count = column_property( #when we query the model, this property will perform a SELECT, together with the SQLAlchemy func.count() method, to add up the votes
  select([func.count(Vote.id)]).where(Vote.post_id == id))

  user = relationship('User')
  comments = relationship('Comment', cascade='all,delete')
  votes = relationship('Vote', cascade='all,delete')
  #deleting a post from the database also deletes its associated comments 
  #querying for a post will return both these data subsets defined by relationships