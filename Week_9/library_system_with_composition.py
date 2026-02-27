class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def book_info(self):
        return f"{self.title} by {self.author}. ISBN: {self.isbn}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def library_welcome(self):
        return f"Welcome to {self.name}\n"

    def add_book(self, book):
        self.books.append(book)
        return f"Added book: {book.book_info()}\n"

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return f"Removed book: {book.book_info()}\n"
        return f"Book '{title}' not found\n"

    def list_books(self):
        if not self.books:
            return f"No books in {self.name}\n"
        result = f"== CATALOGUE OF BOOKS IN {self.name.upper()} ==\n"
        for i, book in enumerate(self.books, 1):
            result += f"{i}. {book.book_info()}\n"
        return result

    def search_book(self, target_title):
        located = [book for book in self.books
                   if target_title.lower() in book.title.lower()]
        if located:
            result = f"Search returned {len(located)} book(s):\n"
            for book in located:
                result += f"  - {book.book_info()}\n"
            return result
        return f"No books in {self.name} with title '{target_title}'\n"


# Create library
library1 = Library("Berlin Library")

# Add books
book1 = Book("The Road", "Cormac McCarthy", "9783060328680")
print(library1.add_book(book1))

book2 = Book("Roadside Picnic", "Arkady & Boris Strugatsky", "9780575093133")
print(library1.add_book(book2))

book3 = Book("The Magus", "John Fowles", "9780099478355")
print(library1.add_book(book3))

# Welcome to library
print(library1.library_welcome())

# List all books
print(library1.list_books())

# Search for book
print(library1.search_book("The Road"))

# Remove a book and verify it's gone
print(library1.remove_book("Roadside Picnic"))
print(library1.search_book("Roadside Picnic"))