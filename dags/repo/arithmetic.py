import os
from sqlalchemy import Table, select, and_
from loginit import AppLogger,SqlLogger
from repo import connection, engine, session, metadata
from datetime import datetime


def fetch_arithmetic_dag_details():

    try:
        result_proxy = connection.execute(
            Table('airthmetic_job_details', metadata, autoload=True, autoload_with=engine).
            select()
            )
        result_set = result_proxy.fetchall()
        AppLogger.info("Successfully fetched api scheduling details")
        return result_set

    except Exception as ex:
        AppLogger.error("Failed to fetch api scheduling details.Error: "+str(ex))
        return None