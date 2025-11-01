# Описание модуля `simple_container_with_dependencies`

## Сборка образа

```bash
docker build -t simple_container_with_dependencies .
```

## Запуск контейнера

```bash
docker run --rm simple_container_with_dependencies
```

## Запуск несколько раз (для генерации разных данных)

```bash
docker run --rm simple_container_with_dependencies
docker run --rm simple_container_with_dependencies
docker run --rm simple_container_with_dependencies
```