"""
Example DAG demonstrating the usage of labels with different branches.
"""

import pendulum
from airflow.models.dag import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator


def print_message(**kwargs) -> None:
    message = kwargs['message']
    print(message)
    return None


with DAG(
        dag_id='first_dag_workshop',
        schedule="*/2 * * * *",
        start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
        catchup=False,
        tags=["workshop", "hello_world_dag"]
) as dag:
    start = EmptyOperator(task_id='start')
    hello_world = PythonOperator(
        task_id='hello_world',
        python_callable=print_message,
        op_kwargs={"message": "hello_world"}
    )
    end = EmptyOperator(task_id='end')

    start >> hello_world >> end
