from os import getenv
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