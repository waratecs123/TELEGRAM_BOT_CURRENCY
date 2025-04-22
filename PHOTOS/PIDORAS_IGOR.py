from datetime import datetime


class Book:
    def __init__(self, title, author, birth_date, isbn, is_borrowed = False):
        self.title = title
        self.author = author
        self.birth_date = birth_date
        self.isbn = isbn
        self.id_borrowed = is_borrowed

    def borrow(self):
        return 0

    def return_book(self):
        return 0

    def age(self):
        today = datetime.today()
        age = today.year - self.birth_date
        self.y = f"Приблизительный возраст книги: {age}"
        return ""

    def __str__(self):
        return (
            f"Книга: {self.title}\n"
            f"Автор: {self.author}\n"
            f"Год написания: {self.birth_date}\n"
            f"Код: {self.isbn}\n"
            f"Бронь: {self.id_borrowed}\n"
            f"{self.y}\n"
        )

book1 = Book("Dick", "Richard", 1990, 34, True)
print(book1.age())
print(book1.__str__())