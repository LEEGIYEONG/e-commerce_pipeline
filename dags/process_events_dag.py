
from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="process_events_dag",
    start_date=pendulum.datetime(2025, 7, 18, tz="Asia/Seoul"),
    schedule_interval="@daily",
    catchup=False,
    tags=["toss_commerce"],
) as dag:
    preprocess_task = BashOperator(
        task_id="preprocess_events",
        bash_command="python C:/Users/LEEGIYEONG/toss_commerce_pipeline/scripts/preprocess_events.py",
    )
