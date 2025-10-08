from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from src import transform, load_bq, upload_gcs

default_args = {'owner': 'airflow', 'start_date': datetime(2025, 10, 8)}

with DAG('gcp_pipeline', schedule_interval='@daily',
         default_args=default_args, catchup=False) as dag:
    
    t1 = PythonOperator(task_id='transform', python_callable=transform)
    t2 = PythonOperator(task_id='upload_gcs', python_callable=upload_gcs)
    t3 = PythonOperator(task_id='load_bq', python_callable=load_bq)
    
    t1 >> t2 >> t3
    


