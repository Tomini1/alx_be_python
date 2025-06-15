class Book:

    """A Book represents a single library book."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available again."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is not checked out, else False."""
        return not self._is_checked_out

    def __str__(self):
        """Return a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """
    A Library manages a collection of Book instances."""
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by title if it is available.
        If found and available, mark it as checked out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return  # Successfully checked out; exit the method.

    def return_book(self, title):
        """Return a book by title. If found and it was checked out, mark it as available.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return  # Successfully returned the book.
        # Optionally, you might report if the book wasn’t found or is already available.

    def list_available_books(self):
        """Print the list of available books in the library. Each book is printed on a new line."""
        available = False
        for book in self._books:
            if book.is_available():
                print(str(book))
                available = True
        if not available:
            print("No available books at the moment.")
