from airflow import settings
from airflow.models import Connection
import os

connection_list = os.getenv("CONNECTION_LIST").split(",")
for connection_name in connection_list:
    conn = Connection(
        conn_id=connection_name,
        conn_type=os.getenv(connection_name+"_CONN_TYPE"),
        host=os.getenv(connection_name+"_HOST"),
        login=os.getenv(connection_name+"_USER"),
        password=os.getenv(connection_name+"_PASSWORD"),
        port=os.getenv(connection_name+"_PORT"),
        schema=os.getenv(connection_name+"_DB"),
        extra=os.getenv(connection_name+"_EXTRA"),
    ) 
    session = settings.Session
    session.add(conn)
    session.commit()