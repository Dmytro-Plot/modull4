from datetime import datetime
input_date = input("Введіть дату в форматі РРРР-ММ-ДД:"   )

def get_days_from_today(date):
    try:
        # Перетворення рядка дати у об'єкт datetime у форматі 'РРРР-ММ-ДД'
        input_date = datetime.strptime(date, '%Y-%m-%d')
        
        # Отримання поточної дати
        today = datetime.today()

        # Розрахунок різниці у днях
        delta = (input_date - today).days

        # Повернення різниці у днях, як цілого числа
        return delta
    except ValueError:
        # Обробка неправильного формату введених даних.
        print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'")
        return None

# Приклад використання:
result = get_days_from_today(input_date)
if result is not None:
    print(f"Кількість днів від заданої дати до поточної: {result}")