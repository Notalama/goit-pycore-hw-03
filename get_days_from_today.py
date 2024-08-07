from datetime import datetime

def get_days_from_today(date_str):
    try:
        # Перетворюємо рядок у об'єкт datetime
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Невірний формат дати. Використовуйте 'РРРР-ММ-ДД'.")

    delta = datetime.now().date() - date_obj.date()
    return delta.days

print(get_days_from_today('2024-08-01'))  # Виведе 4
print(get_days_from_today('2024-07-28'))  # Виведе 8
print(get_days_from_today('2024-08-05'))  # Виведе 0
print(get_days_from_today('2024-08-10'))  # Виведе -5