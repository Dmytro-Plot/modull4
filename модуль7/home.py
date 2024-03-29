from collections import UserDict
from datetime import datetime, timedelta

def input_error(func): # декоратор для введених команд
    def inner(*args, **kwargs): # опрацювання помилок
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name found"
        except IndexError:
            return "Not found"
        except Exception as e:
            return f"Error: {e}"

    return inner

@input_error
def parse_input(user_input): # ФУНКЦІЯ ПАРСЕРУ КОМАНД
    cmd, *args = user_input.split() # РОЗДІЛЯЄМО ВВЕДЕННЯ НА КОМАНДУ ТА АРГУМЕНТИ
    cmd = cmd.strip().lower() # переводимо в нижній регістр і видаляємо зайві пробіли
    return cmd, *args # ПОВЕРТАЄМО КОМАНДУ І СПИСОК АРГУМЕНТІВ

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
     def __init__(self, value):
        super().__init__(value)

def __str__(self):
    return f"Name: {self.value}"

class Birthday(Field):
     def __init__(self, value):
        try:
            # Додаємо перевірку коректності даних
            birthday = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(birthday)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")      

class Phone(Field):
    def __init__(self, value): # Валідація номера телефону (10 цифр)
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format. Format must be 0970000000")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone): # Додавання телефону до запису
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):  # Видалення телефону з запису
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone): # Редагування телефону в запису
        for i, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                self.phones[i] = Phone(new_phone)
                break

    def find_phone(self, phone): # Пошук телефону в запису
         return str(next((p for p in self.phones if str(p) == phone), None))
    
    def add_birthday(self, birthday):
        if birthday not in map(str, self.birthday):
            self.birthday.append(Birthday(birthday))
            print("Birthday added")
        else:
            return 'Birthday already exist in Addressbook'

    def __str__(self):
        return f"Contact name: {self.name}, phones: {', '.join(str(phone) for phone in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record): # Додавання запису до адресної книги
        self.data[record.name.value] = record

    def find(self, name): # Пошук запису за ім'ям
        return self.data.get(name, None)

    def delete(self, name): # Видалення запису за ім'ям
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(book):
        pass


# Створення нової адресної книги
book = AddressBook()
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book):
    if len(args) != 2:
        return "Error: Invalid number of arguments. Use 'add [name] [phone number]'."
    
    name, phone = args
    record = Record(name)
    record.add_phone(phone)

    book.add_record(record)
    return f"Contact {name} added with phone number {phone}."

@input_error
def change_contact(args, book):
    if args[0] in contacts.keys():
        add_contact(args, book)
    else:
        raise(KeyError)

@input_error
def show_phone(args, book):
    return book[args[0]]

@input_error
def show_all(args, book):
    s=''
    for key in book:
        s+=(f"{key:10} : {book[key]}\n")
    return s


@input_error
def add_birthday(args, book):
    name, birthdays = args
    book[name] = birthdays
    return "Birthdays added."

@input_error
def show_birthday(args, book):
    return book[args[0]]

@input_error
def birthdays(args, book):
    today = datetime.today().date()
    upcoming_birthdays = []

    for ruse in book:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)

        if birthday < today:
            # Якщо день народження вже минув в цьому році, розглядаємо його на наступний рік
                irthday = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday - today).days

        # Перенесення дати привітання на наступний понеділок, якщо день народження припадає на вихідний
        if days_until_birthday > 0 and (today + timedelta(days_until_birthday)).weekday() > 4:
                days_until_birthday += (7 - (today + timedelta(days_until_birthday)).weekday())

        if 0 <= days_until_birthday <= 7:
            congratulation_date = today + timedelta(days_until_birthday)
            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})

    return upcoming_birthdays


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args,book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()