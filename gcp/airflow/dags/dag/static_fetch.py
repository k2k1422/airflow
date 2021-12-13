from airflow.operators.python_operator import PythonOperator
import datetime
from tasks import fetch_data,update_data
import random
from airflow import DAG
from datetime import datetime, timedelta


default_args = {
    "owner" : "airflow"
    }

name = "static_fetch"
with DAG(
    name ,
    description = name + "_task",
    tags = ['example'],
    start_date=datetime(2021, 12, 11),
    schedule_interval = "@once",
    default_args = default_args,
    is_paused_upon_creation = False,
    catchup = False
    ) as dag:

    
    update_data_fun = PythonOperator(
        task_id = name+"_updating",
        python_callable = update_data.update_data,
        dag = dag,
        op_kwargs = {}
    )

    l1=[]

    for i in range(10):
        fetch_data_fun = PythonOperator(
                task_id = name+"_fetching_data_"+str(i+1),
                python_callable = fetch_data.fetch_data,
                dag = dag,
                op_kwargs = {
                            'url':'https://httpbin.org/uuid',
                            'no_of_request':10
                            }
            )
        
        update_data_fun.set_upstream(fetch_data_fun)
