# lms_ui.py
# Handles menus and user input/output

from classes import Book, User, Author

class LMS_UI:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    # ----------------- Book Operations -----------------
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        genre = input("Enter genre: ")
        pub_date = input("Enter publication date: ")
        new_book = Book(title, author, genre, pub_date)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully.\n")

    def borrow_book(self):
        book_title = input("Enter the title of the book to borrow: ")
        user_id = input("Enter your library ID: ")
        book = next((b for b in self.books if b.get_title() == book_title), None)
        user = next((u for u in self.users if u.get_library_id() == user_id), None)

        if not book:
            print("Book not found.\n")
            return
        if not user:
            print("User not found.\n")
            return
        if book.get_status() == "Borrowed":
            print("Book is currently borrowed.\n")
            return

        book.set_status("Borrowed")
        user.borrow_book(book_title)
        print(f"Book '{book_title}' borrowed successfully.\n")

    def return_book(self):
        book_title = input("Enter the title of the book to return: ")
        user_id = input("Enter your library ID: ")
        book = next((b for b in self.books if b.get_title() == book_title), None)
        user = next((u for u in self.users if u.get_library_id() == user_id), None)

        if not book or not user:
            print("Book or User not found.\n")
            return
        if book.get_status() == "Available":
            print("Book is not borrowed.\n")
            return

        book.set_status("Available")
        user.return_book(book_title)
        print(f"Book '{book_title}' returned successfully.\n")

    def search_book(self):
        book_title = input("Enter the book title to search: ")
        book = next((b for b in self.books if b.get_title() == book_title), None)
        if book:
            print(book.display_book_info() + "\n")
        else:
            print("Book not found.\n")

    def display_books(self):
        if not self.books:
            print("No books available.\n")
            return
        print("All Books:")
        for book in self.books:
            print(book.display_book_info())
        print()

    # ----------------- User Operations -----------------
    def add_user(self):
        name = input("Enter user name: ")
        library_id = input("Enter library ID: ")
        new_user = User(name, library_id)
        self.users.append(new_user)
        print(f"User '{name}' added successfully.\n")

    def view_user(self):
        user_id = input("Enter user library ID: ")
        user = next((u for u in self.users if u.get_library_id() == user_id), None)
        if user:
            print(user.display_user_info() + "\n")
        else:
            print("User not found.\n")

    def display_users(self):
        if not self.users:
            print("No users available.\n")
            return
        print("All Users:")
        for user in self.users:
            print(user.display_user_info())
        print()

    # ----------------- Author Operations -----------------
    def add_author(self):
        name = input("Enter author name: ")
        bio = input("Enter author biography: ")
        new_author = Author(name, bio)
        self.authors.append(new_author)
        print(f"Author '{name}' added successfully.\n")

    def view_author(self):
        name = input("Enter author name: ")
        author = next((a for a in self.authors if a.get_name() == name), None)
        if author:
            print(author.display_author_info() + "\n")
        else:
            print("Author not found.\n")

    def display_authors(self):
        if not self.authors:
            print("No authors available.\n")
            return
        print("All Authors:")
        for author in self.authors:
            print(author.display_author_info())
        print()

    # ----------------- Menus -----------------
    def book_menu(self):
        while True:
            print("Book Operations:")
            print("1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Back to main menu")
            choice = input("Select an option: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.search_book()
            elif choice == "5":
                self.display_books()
            elif choice == "6":
                break
            else:
                print("Invalid choice.\n")

    def user_menu(self):
        while True:
            print("User Operations:")
            print("1. Add a new user\n2. View user details\n3. Display all users\n4. Back to main menu")
            choice = input("Select an option: ")
            if choice == "1":
                self.add_user()
            elif choice == "2":
                self.view_user()
            elif choice == "3":
                self.display_users()
            elif choice == "4":
                break
            else:
                print("Invalid choice.\n")

    def author_menu(self):
        while True:
            print("Author Operations:")
            print("1. Add a new author\n2. View author details\n3. Display all authors\n4. Back to main menu")
            choice = input("Select an option: ")
            if choice == "1":
                self.add_author()
            elif choice == "2":
                self.view_author()
            elif choice == "3":
                self.display_authors()
            elif choice == "4":
                break
            else:
                print("Invalid choice.\n")

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("Main Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
            choice = input("Select an option: ")
            if choice == "1":
                self.book_menu()
            elif choice == "2":
                self.user_menu()
            elif choice == "3":
                self.author_menu()
            elif choice == "4":
                print("Exiting Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice.\n")

