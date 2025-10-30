# Описание модуля `simple_container_with_args`

## Сборка образа

```bash
docker build -t simple_container_with_args .
```

## Запуск без аргументов (дефолтное значение)

```bash
docker run --rm simple_container_with_args
```

## Запуск с коротким флагом `-m`

```bash
docker run --rm simple_container_with_args -m "ETL pipeline завершён успешно ✅"
```

## Запуск с полным названием `--message`

```bash
docker run --rm simple_container_with_args --message "Данные загружены в таблицу users"
```

## Просмотр справки

```bash
docker run --rm simple_container_with_args --help
```