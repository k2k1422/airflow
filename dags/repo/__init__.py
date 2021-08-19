from dotenv import load_dotenv
import os
import logging
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from loginit import AppLogger,SqlLogger

# try:
#     load_dotenv(verbose=True)
# except Exception as ex:
#     AppLogger.error("Failed to load the env file")

try:
    engine = create_engine(os.getenv("PY_REPO_URI"))
    connection = engine.connect()
    
    Session = sessionmaker(bind = engine)
    session = Session()
    metadata = MetaData(schema = os.getenv("REPO_SCHEMA"))
    
except Exception as ex:
    AppLogger.error("Failed to connect to application database.Error: "+str(ex))