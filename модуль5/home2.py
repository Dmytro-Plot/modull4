import re
from typing import Callable

def generator_numbers(text: str):
    # Визначення регулярного виразу для пошуку дійсних чисел
    pattern = re.compile(r'\b\d+(\.\d+)?\b')
    
    # Пошук у тексті за допомогою регулярного виразу та використання yield для створення генератора
    for match in pattern.finditer(text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    # Виклик функції-генератора та підсумовування чисел
    total_sum = sum(func(text))
    return total_sum

# Приклад
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")