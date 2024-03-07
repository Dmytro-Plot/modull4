from collections import UserDict

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

class Phone(Field):
    def __init__(self, value): # Валідація номера телефону (10 цифр)
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format. Format must be 0970000000")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

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


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name.value}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
