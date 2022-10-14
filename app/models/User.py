from app.db import Base
import bcrypt #we want to directly use the bcrypt module so the import syntax differs 
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates

salt = bcrypt.gensalt()
#create user class that inherits from Base class
#Base class was created as part of db package
#in the User class we declare properties that the Base class will use to make the table
#we use classes from the sqlalchemy module to define the table columns and their data types
#we can also give options to each column
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)
#we add a new validate_email() method to the class that 
#a @validates('email') decorator wraps
#the validate_email() method returns what the value of the email column should be
#the @validates('email') decorator internally handles the rest
#the assert keyword is used to check if an email address contains an at-sign character (@)
#the assert keyword automatically throws an error if the condition is false, thus preventing the return statement from happening
# make sure email address contains @ character
  @validates('email')
  def validate_email(self, key, email):
    assert '@' in email

    return email

  @validates('password')
  def validate_password(self, key, password):
    assert len(password) > 4

  
    return bcrypt.hashpw(password.encode('utf-8'), salt)
#return an encrypted version of the password, if the assert doesnt throw an error
  def verify_password(self, password):
    return bcrypt.checkpw(
      password.encode('utf-8'),
      self.password.encode('utf-8')
  ) #uses checkpw() method to compare the incoming password parameter to the one saved on the User object (self.password)


