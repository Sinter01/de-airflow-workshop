# de-workshop-airflow
полезные ссылки:
1. Описание запуска airflow через docker-compose: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
2. Сам файл docker-compose.yaml: https://airflow.apache.org/docs/apache-airflow/2.10.4/docker-compose.yaml
3. Архитектура: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html#airflow-components
4. Версии базового образа airflow (можно найти с необходимой версией python)  https://hub.docker.com/r/apache/airflow/tags
5. Про крон-строку подробно  https://crontab.guru/
6. Сервис прогноза погоды Free Weather API https://www.weatherapi.com/api-explorer.aspx#forecast
---
Запуск airflow локально
1. git clone de-workshop-airflow
2. docker-compose up -d
3. Создать Postgres connection dwh, Variable FREE_WEATHER_API_TOKEN
