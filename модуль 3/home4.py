from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)

        if birthday < today:
            # Якщо день народження вже минув в цьому році, розглядаємо його на наступний рік
            birthday = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday - today).days

        # Перенесення дати привітання на наступний понеділок, якщо день народження припадає на вихідний
        if days_until_birthday > 0 and (today + timedelta(days_until_birthday)).weekday() > 4:
            days_until_birthday += (7 - (today + timedelta(days_until_birthday)).weekday())

        if 0 <= days_until_birthday <= 7:
            congratulation_date = today + timedelta(days_until_birthday)
            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})

    return upcoming_birthdays

# Приклад використання:
users = [
    {"name": "John Doe", "birthday": "1985.01.28"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)