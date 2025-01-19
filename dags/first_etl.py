import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from utils import etl

with DAG(
        dag_id='weather_etl',
        schedule="*/2 * * * *",
        start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
        catchup=False,
        tags=["workshop", "weather"]
) as dag:
    etl = PythonOperator(
        task_id='weather_etl',
        python_callable=etl,
        op_kwargs={"city": "Moscow"}
    )
    etl
