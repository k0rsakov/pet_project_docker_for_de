import argparse

def main():
    # Создаём парсер аргументов
    parser = argparse.ArgumentParser(
        description='ETL контейнер с аргументами командной строки'
    )

    parser.add_argument(
        '-m', '--message',
        type=str,
        default='Дефолтное сообщение: ETL процесс не запущен',
        help='Сообщение о статусе ETL процесса'
    )

    args = parser.parse_args()

    print("=" * 60)
    print("📊 ETL PROCESS STATUS")
    print("=" * 60)
    print(f"{args.message}")
    print("=" * 60)

if __name__ == "__main__":
    main()