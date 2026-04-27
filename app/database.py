from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
SQLALCHEMY_DATABASE_URL = (f'postgresql://{settings.database_username}:{settings.database_password}'
                           f'@{settings.database_hostname}/{settings.database_name}')

engine = create_engine(SQLALCHEMY_DATABASE_URL) #establishes a connection

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #creates a session for communication

Base = declarative_base() #all the models that we will use to create tables will inherit from this base class

def get_db(): #dependency
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()