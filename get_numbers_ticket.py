import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка валідності параметрів
    if (min < 1 or min > max or max < 0 or max > 1000):
        return []
    
    numbers = set()

    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(list(numbers))

print(get_numbers_ticket(50, 333, 10))
print(get_numbers_ticket(-2, 333, 10))