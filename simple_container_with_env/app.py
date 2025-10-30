import os


def main():
    # Получаем переменные окружения
    db_host = os.getenv("DB_HOST", "localhost")
    db_name = os.getenv("DB_NAME", "default_db")
    db_port = os.getenv("DB_PORT", "5432")
    db_user = os.getenv("DB_USER", "admin")

    print("=" * 60)
    print("🗄️  DATABASE CONNECTION CONFIG")
    print("=" * 60)
    print(f"Host: {db_host}")
    print(f"Database: {db_name}")
    print(f"Port: {db_port}")
    print(f"User: {db_user}")
    print("=" * 60)
    print("✅ Конфигурация загружена успешно!")
    print("=" * 60)


if __name__ == "__main__":
    main()
