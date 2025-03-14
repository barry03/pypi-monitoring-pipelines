from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

# Configuration du DAG
default_args = {
    "owner": "Test-Oscaro",
    "depends_on_past": False,
    "start_date": days_ago(1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "pypi_data_pipeline",
    default_args=default_args,
    description="Pipeline Airflow pour exécuter le script main.py",
    schedule_interval="0 0 * * *",
    catchup=False,
)

run_main = BashOperator(
    task_id="run_main",
    bash_command="PYTHONPATH=/home/airflow/gcs/data/src python /home/airflow/gcs/data/src/main.py",
    dag=dag,
)

run_main