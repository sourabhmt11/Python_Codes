from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1)
    }

with DAG(
    dag_id='run_python_script_dag',
    default_args=default_args,
    schedule_interval='@daily',  # Change as needed
    catchup=False,
    tags=['example'],
) as dag:

    run_script = BashOperator(
        task_id='run_my_python_script',
        bash_command='python /opt/airflow/scripts/my_script.py'
    )