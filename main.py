from datetime import datetime, timedelta
from collections import defaultdict
from faker import Faker
from faker.providers import person

fake = Faker()
fake.add_provider(person)
Faker.seed(0)

person_list = []

for i in range(1000):
    person_list.append({"name": fake.name(), "birthday": fake.date_of_birth()})


def get_period() -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    start_date = current_date + timedelta(days=5 - current_date.weekday())
    end_date = start_date + timedelta(days=6)
    return start_date.date(), end_date.date()


def check_empl(list_of_empl: list) -> defaultdict:
    result = defaultdict(list)
    current_year = datetime.now().year

    start, end = get_period()

    for empl in list_of_empl:
        bd_year = empl["birthday"].year
        bd = empl["birthday"]
        if empl["birthday"].day == 29 and empl["birthday"].month == 2:
            if (bd_year % 400 == 0 and bd_year % 100 == 0) or (
                bd_year % 4 == 0 and bd_year % 100 != 0
            ):
                bd = bd.replace(day=28)
        bd = bd.replace(year=current_year)

        if start <= bd <= end:
            if bd.weekday() in [5, 6]:
                result[0].append(empl["name"])

            else:
                result[bd.weekday()].append(empl["name"])

    return result


week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def get_birthdays_per_week(employees_to_greet: dict) -> None:
    global week_days
    for i, value in enumerate(week_days):
        if employees_to_greet.get(i):
            text = ", ".join(employees_to_greet[i])
            print(f"{value} : {text} ")


if __name__ == "__main__":
    spisok = check_empl(person_list)
    get_birthdays_per_week(spisok)
