# Описание модуля `simple_airflow_with_own_simple_container_with_env`

## Получение docker-compose для Airflow

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.4/docker-compose.yaml'
```

## Запуск Airflow

```bash
docker-compose up -d
```

## Перезапуск Airflow

```bash
docker-compose down && docker-compose up -d
```

## Проверка подключённого локально docker daemon

Заходим в контейнер worker:

```bash
docker exec -it simple_airflow_with_own_simple_container_with_env-airflow-worker-1 bash
```

Внутри контейнера проверяем доступные образы:

```bash
docker images
```
