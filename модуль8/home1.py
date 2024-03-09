import pickle
from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        # Реалізація додавання запису

    def find(self, name):
        # Реалізація пошуку запису

    def delete(self, name):
        # Реалізація видалення запису

    def save_data(self, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self.data, f)

    def load_data(self, filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            self.data = {}

# Функції для серіалізації та десеріалізації з використанням pickle
def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book.data, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
            book = AddressBook()
            book.data = data
            return book
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()

    # Основний цикл програми

    book.save_data()  # Викликати перед виходом з програми
