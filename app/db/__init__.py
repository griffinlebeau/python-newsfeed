from os import getenv
from flask import g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
#the getenv() function is part of Python's built-in os module
#but because we used a .env file to fake the environment variable
#we need to first call load_dotenv() from the python-dotenv module
#in production, DB_URL will be a proper environment variable
load_dotenv()

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()
#engine variable manages the overall connection to the db
#Session variable generates temporary connections for perofrming CRUD operations
#Base class variable helps us map the models to real MySQL tables

def init_db(app): #same Base method from seeds.py file, but we wont call it until after we've called init_db() once the Flask app is ready
  Base.metadata.create_all(engine)
#tells flask to run close_db() with its built-in teardown_appcontext() method
  app.teardown_appcontext(close_db)

def get_db():
  if 'db' not in g:
    #saves the current connection on the g object, if its not already there, then returns the connection from the g object instead of creating a new Session isntance each time
    g.db = Session()

  return g.db

def close_db(e=None):
  db = g.pop('db', None) #attempts to find and remove db from the g object
    #if db exists, then db.close() will end the connection
  if db is not None:
    db.close()
#Flask creates a new context eery time a server request is made
#When the request ends, the context is removed from the app
#These temporary contexts provide global variables like the g object, that can be
#shared across modules as long as the context is still active 