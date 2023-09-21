class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def display_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            print("\nAvailable Books:")
            for book in available_books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        else:
            print("\nNo books are currently available in the library.")

    def check_out_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_available:
                    book.is_available = False
                    print(f"Checked out '{book.title}'")
                else:
                    print(f"'{book.title}' is already checked out.")
                return
        print("Book not found in the library.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_available:
                    book.is_available = True
                    print(f"Returned '{book.title}'")
                else:
                    print(f"'{book.title}' is already in the library.")
                return
        print("Book not found in the library.")

# User interface code
library = Library()

while True:
    print("\nLibrary Management System Menu:")
    print("1. Add a book")
    print("2. List available books")
    print("3. Check out a book")
    print("4. Return a book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        new_book = Book(title, author, isbn)
        library.add_book(new_book)

    elif choice == "2":
        library.display_available_books()

    elif choice == "3":
        isbn = input("Enter ISBN of the book to check out: ")
        library.check_out_book(isbn)

    elif choice == "4":
        isbn = input("Enter ISBN of the book to return: ")
        library.return_book(isbn)

    elif choice == "5":
        print("Exiting Library Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
