# Library Management System

## Overview
The **Library Management System (LMS)** is a command-line-based Python application designed to streamline the management of books, authors, and users in a library. This system demonstrates **Object-Oriented Programming (OOP) principles**, including **encapsulation**, **modularity**, and **class interactions**.

Users can add, borrow, return, search, and display books; manage library users; and manage authors efficiently through a user-friendly menu interface.

---

## Features

### Book Operations
- Add a new book with details: title, author, genre, publication date.
- Borrow a book (marks it as "Borrowed").
- Return a book (marks it as "Available").
- Search for a book by title.
- Display all books.

### User Operations
- Add a new user with a name and library ID.
- View user details, including borrowed books.
- Display all users.

### Author Operations
- Add a new author with name and biography.
- View author details.
- Display all authors.

### Design Principles
- **Object-Oriented Programming**: Classes for Book, User, and Author.
- **Encapsulation**: Private attributes with getters and setters.
- **Modular Design**: Separate files for classes (classes.py), user interface (lms_ui.py), and main execution (main.py).
- **Error Handling**: Graceful handling of invalid inputs.
- **Interactive CLI**: Menus for easy navigation.

---

## Requirements
- Python 3.x

---

## How to Run
1. Clone the repository:
    git clone https://github.com/tip46985-cloud/library_management_assignment.git
2. Navigate to the project folder:
    cd library_management_assignment
3. Run the main application:
    python main.py
4. Follow the on-screen menus to perform operations.

---

## Optional Enhancements
- File Handling: Save and load data from text files for books, users, and authors.
- Reservation System: Reserve books and notify users when available.
- Fine Calculation: Compute fines for overdue books.

---

## Project Structure
library_management_assignment/
├─ classes.py
├─ lms_ui.py
├─ main.py
└─ README.md

---

## GitHub Repository
https://github.com/tip46985-cloud/library_management_assignment

---

## Author
- Your Name
- GitHub: tip46985-cloud
