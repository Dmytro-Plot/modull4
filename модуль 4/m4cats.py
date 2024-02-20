def get_cats_info(path):
    try:
        cats_info = []

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на ідентифікатор, ім'я та вік кота
                parts = line.strip().split(',')
                if len(parts) == 3:
                    # Створюємо словник для кота та додаємо його до списку
                    cat_info = {"id": parts[0], "name": parts[1], "age": parts[2]}
                    cats_info.append(cat_info)

        return cats_info

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return []

# Використання
cats_info = get_cats_info(r"e:/Projects/модуль 4/cats_file.txt")
print(cats_info)