from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    """
    Визначає користувачів, яких потрібно привітати з днем народження протягом наступного тижня.

    Аргументи:
        users: Список словників, де кожен словник містить ключі 'name' (ім'я) та 'birthday' (дата народження у форматі 'рік.місяць.дата').

    Повертає:
        Список словників, де кожен словник містить ключі 'name' (ім'я) та 'congratulation_date' (дата привітання у форматі 'рік.місяць.дата').
    """

    upcoming_birthdays = []
    today = datetime.today().date()

    for user in users:
        # Перетворюємо рядок дати народження в об'єкт datetime.date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув цього року, розглядаємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Розраховуємо різницю між днем народження та поточною датою
        days_until_birthday = (birthday_this_year - today).days

        # Перевіряємо, чи день народження випадає на наступний тиждень (7 днів)
        if 0 <= days_until_birthday <= 7:
            # Якщо день народження на вихідні, переносимо привітання на понеділок
            congratulation_date = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()) % 7)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays

# Приклад використання:
users = [
    {"name": "John Doe", "birthday": "1985.08.03"},
    {"name": "Jane Smith", "birthday": "1990.08.04"},
    {"name": "Alice Johnson", "birthday": "1995.08.10"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
