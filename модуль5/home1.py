def caching_fibonacci():
    # Створення порожнього словника для зберігання результатів обчислення Фібоначчі
    cache = {}

    # Внутрішня функція для обчислення числа Фібоначчі з використанням кешу
    def fibonacci(n):
        # Якщо n <= 0, повертаємо 0
        if n <= 0:
            return 0
        # Якщо n == 1, повертаємо 1
        elif n == 1:
            return 1
        # Якщо n у кеші, повертаємо значення з кешу
        elif n in cache:
            return cache[n]
        # Якщо n не у кеші, обчислюємо його рекурсивно та зберігаємо у кеш
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result
            return result

    # Повертаємо внутрішню функцію для використання
    return fibonacci

# Приклад
fib = caching_fibonacci()
print(fib(0))  # Виведе 55
print(fib(-1))  # Виведе 610