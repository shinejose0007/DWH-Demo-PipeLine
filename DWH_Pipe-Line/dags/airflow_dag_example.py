
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'demo',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract(**context):
    # placeholder: extract from DWH (e.g. read csv / query DB)
    pass

def transform(**context):
    # placeholder: run transform function and save processed data
    pass

def train(**context):
    # placeholder: train model and save artifact
    pass

with DAG('demo_etl_ml_pipeline', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    t1 = PythonOperator(task_id='extract', python_callable=extract)
    t2 = PythonOperator(task_id='transform', python_callable=transform)
    t3 = PythonOperator(task_id='train', python_callable=train)
    t1 >> t2 >> t3
