import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка валідності вхідних параметрів
    if not (1 <= min <= max <= 1000 and 1 <= quantity <= max - min + 1):
        print("Невірні вхідні параметри.")
        return []

    # Генерація унікальних чисел
    unique_numbers = set()
    while len(unique_numbers) < quantity:
        unique_numbers.add(random.randint(min, max))

    # Повернення відсортованого списку
    return sorted(list(unique_numbers))

# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)