from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey
#doesnt need to store any unique information 
#post model will count the votes
class Vote(Base):
  __tablename__ = 'votes'
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  post_id = Column(Integer, ForeignKey('posts.id'))