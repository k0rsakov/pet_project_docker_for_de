# Описание модуля `simple_container_with_env`

## Сборка образа

```bash
docker build -t simple_container_with_env .
```

## Запуск без переменных (использовать дефолтные значения из Dockerfile)

```bash
docker run simple_container_with_env
```

## Запуск с переменными через флаг `-e`

```bash
docker run -e DB_HOST=prod-server -e DB_NAME=analytics simple_container_with_env
```

## Запуск с несколькими переменными

```bash
docker run \
  -e DB_HOST=prod-server.example.com \
  -e DB_NAME=analytics_db \
  -e DB_PORT=5432 \
  -e DB_USER=data_engineer \
  simple_container_with_env
```

## Запуск с `.env` файлом

```bash
docker run --env-file .env simple_container_with_env
```