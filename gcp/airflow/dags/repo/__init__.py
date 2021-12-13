# from dotenv import load_dotenv
import os
import logging
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
# from loginit import AppLogger,SqlLogger
from airflow import settings
from airflow.models import Connection
import os
# try:
#     load_dotenv(verbose=True)
# except Exception as ex:
#     AppLogger.error("Failed to load the env file")

print("Inside repo folder init")

engine = create_engine(os.getenv("AIRFLOW_CONN_MY_PROD_DATABASE"))
connection = engine.connect()

Session = sessionmaker(bind = engine)
session = Session()
metadata = MetaData(schema = os.getenv("REPO_SCHEMA"))

# try:
#     session = settings.Session
#     connection_list = os.getenv("CONNECTION_LIST").split(",")
#     for connection_name in connection_list:
#         connection_query = session.query(Connection).filter(Connection.conn_id == connection_name,)
#         connection_query_result = connection_query.one_or_none()
#         if not connection_query_result:   
#             conn = Connection(
#                 conn_id=connection_name,
#                 conn_type=os.getenv(connection_name+"_CONN_TYPE"),
#                 host=os.getenv(connection_name+"_HOST"),
#                 login=os.getenv(connection_name+"_USER"),
#                 password=os.getenv(connection_name+"_PASSWORD"),
#                 port=os.getenv(connection_name+"_PORT"),
#                 schema=os.getenv(connection_name+"_DB"),
#                 extra=os.getenv(connection_name+"_EXTRA"),
#             ) 
#             session = settings.Session
#             session.add(conn)
#             session.commit()
# except Exception as e:
#     AppLogger.info(
#         "Failed creating connection")
#     AppLogger.info(e)