import re

def normalize_phone(phone_number):
    """
    Нормалізує телефонний номер до стандартного міжнародного формату.

    Аргументи:
        phone_number: Рядок з телефонним номером у будь-якому форматі.

    Повертає:
        Нормалізований телефонний номер у форматі '+380xxxxxxxxx',
        де xxxxxxxxxx - цифри номера.
    """

    # Видалення всіх символів, крім цифр та '+'
    digits_only = re.sub(r'[^\d+]', '', phone_number)

    # Перевірка та корекція префіксу
    if digits_only.startswith('+'):
        # Якщо номер вже має '+', залишаємо його без змін
        normalized_number = digits_only
    elif digits_only.startswith('380'):
        # Якщо номер починається з '380', додаємо '+' на початок
        normalized_number = '+' + digits_only
    else:
        # Якщо номер не має коду країни, додаємо '+38'
        normalized_number = '+38' + digits_only

    return normalized_number

# Приклад використання (з вашими даними):
raw_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
