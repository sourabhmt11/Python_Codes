from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def my_custom_script():
    print("Hello from Airflow Python Script!")

default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG('hello_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    task = PythonOperator(
        task_id='run_my_script',
        python_callable=my_custom_script
    )
