def total_salary(path):
    try:
        total_salary = 0
        total_count = 0

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на прізвище та зарплату
                parts = line.strip().split(',')
                if len(parts) == 2:
                    # Додаємо зарплату до загальної суми
                    total_salary += int(parts[1])
                    total_count += 1

        # Розраховуємо середню зарплату
        average_salary = total_salary / total_count if total_count > 0 else 0

        return total_salary, average_salary

    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return 0, 0

# використання
total, average = total_salary(r"e:/Projects/модуль 4/total_salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")