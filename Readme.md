Project Overview
The Book Catalog App is a Python-based desktop application built using the PyQt5 library. This application allows users to manage their book collection. Users can add, update, delete, search, and view books in the catalog. The app also features a toggle to mark books as "Read" or "Unread" and enables sorting of books by various criteria such as title, author, year of publication, and genre.

Key Features:
Add new books with details such as title, author, genre, year, ISBN, pages, pages read, and reading status.
View a list of all books in a table with sorting capabilities.
Update book details and mark books as "Read" or "Unread".
Search for books by title or author.
Delete books from the catalog.

Installation
Requirements:
Python 3.6 or higher
PyQt5
SQLite (used for local database)

git clone https://github.com/NDONGONGA/book-catalog-app.git

pip install pyqt5

Set up the database: The application uses SQLite for data storage. Upon running the app for the first time, the database file books.db will be created automatically.

Run the application: To start the application, run:

python main.py
