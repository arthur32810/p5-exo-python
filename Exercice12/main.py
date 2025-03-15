class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    # Ajouter les méthodes ici

    def add_book(self, book):
        self.book.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return True
        return False

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.borrow_books.append(book)
                self.books.remove(book)
                return True
        return False

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.books.append(book)
                self.borrow_books.remove(book)
                return True
        return False

    def available_books(self):
        for book in self.books:
            print(f"{book.title}")

    def borrowed_books(self):
        for book in self.borrow_books:
            print(f"{book.title}")
