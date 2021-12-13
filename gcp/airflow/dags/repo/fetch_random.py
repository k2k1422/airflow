import os
from sqlalchemy import Table, select, and_
# from loginit import AppLogger,SqlLogger
# from repo import connection, engine, session, metadata
from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
# from loginit import AppLogger,SqlLogger
from airflow import settings
from airflow.models import Connection


def fetch_random_details():

    try:
        engine = create_engine("postgresql+psycopg2://postgres:docker@localhost:5432/application")
        connection = engine.connect()

        Session = sessionmaker(bind = engine)
        session = Session()
        metadata = MetaData(schema = os.getenv("REPO_SCHEMA"))
        result_proxy = connection.execute(
            Table('fetch_randam', metadata, autoload=True, autoload_with=engine).
            select()
            )
        result_set = result_proxy.fetchall()
        # AppLogger.info("Successfully fetched api scheduling details")
        return result_set

    except Exception as ex:
        # AppLogger.error("Failed to fetch api scheduling details.Error: "+str(ex))
        print("inside repo exception")
        return None