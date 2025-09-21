# classes.py
# Defines Book, User, and Author classes with encapsulation

class Book:
    def __init__(self, title, author, genre, pub_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__pub_date = pub_date
        self.__status = "Available"

    # Getters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_pub_date(self):
        return self.__pub_date

    def get_status(self):
        return self.__status

    # Setters
    def set_status(self, status):
        if status in ["Available", "Borrowed"]:
            self.__status = status

    def display_book_info(self):
        return f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Published: {self.__pub_date}, Status: {self.__status}"


class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    # Getters
    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    # Borrow and return books
    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)

    def display_user_info(self):
        borrowed = ', '.join(self.__borrowed_books) if self.__borrowed_books else 'None'
        return f"Name: {self.__name}, ID: {self.__library_id}, Borrowed Books: {borrowed}"


class Author:
    def __init__(self, name, bio):
        self.__name = name
        self.__bio = bio

    # Getters
    def get_name(self):
        return self.__name

    def get_bio(self):
        return self.__bio

    def display_author_info(self):
        return f"Author: {self.__name}, Biography: {self.__bio}"

