FROM apache/airflow:2.10.4-python3.12
ADD requirements.txt .
RUN pip install -r requirements.txt