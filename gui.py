from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit, QComboBox, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout, QHeaderView
)
from db import add_book, get_books, search_books, delete_book, update_book


class BookCatalogApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Book Catalog")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet(self.get_stylesheet())
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Form Fields
        form_layout = QFormLayout()
        self.title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.genre_input = QLineEdit()
        self.year_input = QLineEdit()
        self.isbn_input = QLineEdit()
        self.pages_input = QLineEdit()
        self.pages_read_input = QLineEdit()
        self.status_input = QComboBox()
        self.status_input.addItems(["Unread", "Currently Reading", "Read"])

        form_layout.addRow("Title:", self.title_input)
        form_layout.addRow("Author:", self.author_input)
        form_layout.addRow("Genre:", self.genre_input)
        form_layout.addRow("Year:", self.year_input)
        form_layout.addRow("ISBN:", self.isbn_input)
        form_layout.addRow("Pages:", self.pages_input)
        form_layout.addRow("Pages Read:", self.pages_read_input)
        form_layout.addRow("Status:", self.status_input)
        layout.addLayout(form_layout)

        # Buttons
        button_layout = QHBoxLayout()
        self.add_btn = QPushButton("Add Book")
        self.update_btn = QPushButton("Update Book")
        self.delete_btn = QPushButton("Delete Book")
        self.search_input = QLineEdit()
        self.search_btn = QPushButton("Search")

        self.add_btn.clicked.connect(self.add_book)
        self.update_btn.clicked.connect(self.update_selected_book)
        self.delete_btn.clicked.connect(self.delete_selected_book)
        self.search_btn.clicked.connect(self.search_books)

        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.update_btn)
        button_layout.addWidget(self.delete_btn)
        button_layout.addWidget(self.search_input)
        button_layout.addWidget(self.search_btn)
        layout.addLayout(button_layout)

        # Table to Display Books
        self.book_table = QTableWidget()
        self.book_table.setColumnCount(7)
        self.book_table.setHorizontalHeaderLabels(["ID", "Title", "Author", "Genre", "Year", "Status", "ISBN"])
        self.book_table.cellClicked.connect(self.load_selected_book)

        # Enable sorting when clicking on headers
        self.book_table.setSortingEnabled(True)
        self.book_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        layout.addWidget(self.book_table)

        self.setLayout(layout)
        self.load_books()

    def get_stylesheet(self):
        return """
            QWidget {
                background-color: white;
                font-family: 'Arial';
                font-size: 14px;
            }
            QPushButton {
                background-color: #0078D7;
                color: white;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #005BB5;
            }
            QLineEdit, QComboBox {
                border: 1px solid #0078D7;
                padding: 5px;
                border-radius: 3px;
            }
            QTableWidget {
                background-color: #f0f8ff;
                border: 1px solid #0078D7;
                gridline-color: #0078D7;
            }
            QHeaderView::section {
                background-color: #0078D7;
                color: white;
                font-weight: bold;
            }
        """

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        genre = self.genre_input.text()
        year = self.year_input.text()
        isbn = self.isbn_input.text()
        pages = self.pages_input.text()
        pages_read = self.pages_read_input.text()
        status = self.status_input.currentText()

        if not title or not author:
            QMessageBox.warning(self, "Error", "Title and Author cannot be empty!")
            return

        add_book(title, author, genre, year, isbn, pages, pages_read, status)
        self.load_books()

    def update_selected_book(self):
        selected_row = self.book_table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a book to update.")
            return

        book_id = self.book_table.item(selected_row, 0).text()
        title = self.title_input.text()
        author = self.author_input.text()
        genre = self.genre_input.text()
        year = self.year_input.text()
        isbn = self.isbn_input.text()
        pages = self.pages_input.text()
        pages_read = self.pages_read_input.text()
        status = self.status_input.currentText()

        update_book(book_id, title, author, genre, year, isbn, pages, pages_read, status)
        QMessageBox.information(self, "Success", "Book details updated successfully.")
        self.load_books()

    def delete_selected_book(self):
        selected_row = self.book_table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a book to delete.")
            return

        book_id = self.book_table.item(selected_row, 0).text()
        delete_book(book_id)
        QMessageBox.information(self, "Success", "Book deleted successfully.")
        self.load_books()

    def search_books(self):
        keyword = self.search_input.text()
        books = search_books(keyword)
        self.populate_table(books)

    def load_books(self):
        books = get_books()
        self.populate_table(books)

    def populate_table(self, books):
        self.book_table.setRowCount(len(books))
        for row, book in enumerate(books):
            for col, item in enumerate(book):
                self.book_table.setItem(row, col, QTableWidgetItem(str(item)))

    def load_selected_book(self, row):
        self.title_input.setText(self.book_table.item(row, 1).text())
        self.author_input.setText(self.book_table.item(row, 2).text())
        self.genre_input.setText(self.book_table.item(row, 3).text())
        self.year_input.setText(self.book_table.item(row, 4).text())
        self.status_input.setCurrentText(self.book_table.item(row, 5).text())
        self.isbn_input.setText(self.book_table.item(row, 6).text())

    def toggle_read_status(self):
        selected_row = self.book_table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a book to mark as read/unread.")
            return

        book_id = self.book_table.item(selected_row, 0).text()
        current_status = self.book_table.item(selected_row, 5).text()  # Corrected column index

        # Toggle the status
        new_status = "Read" if current_status != "Read" else "Unread"
        update_book(book_id, self.book_table.item(selected_row, 1).text(), self.book_table.item(selected_row, 2).text(),
                    self.book_table.item(selected_row, 3).text(), self.book_table.item(selected_row, 4).text(),
                    self.book_table.item(selected_row, 6).text(), self.book_table.item(selected_row, 5).text(),  # Corrected
                    self.book_table.item(selected_row, 7).text(), new_status)  # Removed incorrect column access
        self.load_books()  # Reload the list of books to reflect the status change
