from airflow.operators.python_operator import PythonOperator
import datetime
from utils.utils import convert_to_utc
from tasks.arithmetic import add as add_task, power as power_task
import random

def create_airthmetic_dag(DAG,dag_details):

    default_args = {
        "owner" : "airflow"
        }
    start_date = convert_to_utc(dag_details['start_date'])

    if dag_details['load_type'] == 'one_time':
        end_date = None
        interval = '@once'
    else:
        if dag_details['period_indicator'] == 'weeks':
            interval = datetime.timedelta(weeks = dag_details['period_interval'])
        elif dag_details['period_indicator'] == 'days':
            interval = datetime.timedelta(days = dag_details['period_interval'])
        elif dag_details['period_indicator'] == 'hours':
            interval = datetime.timedelta(hours = dag_details['period_interval'])
        elif dag_details['period_indicator'] == 'minutes':
            interval = datetime.timedelta(minutes = dag_details['period_interval'])
        elif dag_details['period_indicator'] == 'seconds':
            interval = datetime.timedelta(seconds = dag_details['period_interval'])

        if dag_details['end_date'] != 0:
            end_date = convert_to_utc(dag_details['end_date'])
        else:
            end_date = None
    name = "arithmetic"+str(dag_details['id'])
    dag = DAG(
        name ,
        description = name + "_arithmetic_task",
        tags = ['api'],
        start_date = start_date,
        end_date = end_date,
        schedule_interval = interval,
        default_args = default_args,
        is_paused_upon_creation = False,
        catchup = False
        )

    add_fun = PythonOperator(
        task_id = name+"_addition",
        python_callable = add_task.add,
        dag = dag,
        op_kwargs = {'a':random.randint(1,100),'b':random.randint(1,100)}
    )
    
    power_fun = PythonOperator(
        task_id = name+"_power",
        python_callable = power_task.power,
        dag = dag,
        op_kwargs = {'a':random.randint(1,100),'b':random.randint(1,100)}
    )
    
    add_fun >> power_fun

    return dag
