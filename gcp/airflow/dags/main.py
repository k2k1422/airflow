from airflow.models import DAG
from repo.fetch_random import fetch_random_details
from utils.utils import convert_result_to_df
from dag.dynamic_fetch import create_fetch_dag

db_dag_details = fetch_random_details()

if db_dag_details:
    db_dag_details_df = convert_result_to_df(db_dag_details)
    print(db_dag_details_df)
    for index, row in db_dag_details_df.iterrows():
        print("Inside main",row['task_name'],row['total_request'],row['chunk_size'])
        globals()[row['task_name']] = create_fetch_dag(row['task_name'],row['total_request'],row['chunk_size'])