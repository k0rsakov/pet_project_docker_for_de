import datetime
import uuid

from faker import Faker

fake = Faker(locale="ru_RU")


dict_ = {
    "id": uuid.uuid4(),
    "created_at": fake.date_time_ad(
        start_datetime=datetime.date(year=2024, month=1, day=1),
        end_datetime=datetime.date(year=2025, month=1, day=1),
    ),
    "first_name": fake.first_name(),
    "last_name": fake.last_name(),
    "middle_name": fake.middle_name(),
    "birthday": fake.date_time_ad(
        start_datetime=datetime.date(year=1980, month=1, day=1),
        end_datetime=datetime.date(year=2005, month=1, day=1),
    ),
    "email": fake.email(),
    "city": fake.city(),
}

print(dict_)