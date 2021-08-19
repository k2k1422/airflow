import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
os.environ["BASE_DIR"] = BASE_DIR

from airflow.models import DAG
from repo.arithmetic import fetch_arithmetic_dag_details
from utils.utils import convert_result_to_df
from dag.arithmetic_dag import create_airthmetic_dag

db_dag_details = fetch_arithmetic_dag_details()
if db_dag_details:
    db_dag_details_df = convert_result_to_df(db_dag_details)
    for index, row in db_dag_details_df.iterrows():
        globals()[row['id']] = create_airthmetic_dag(DAG,row)
