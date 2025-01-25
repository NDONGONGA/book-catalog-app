import sqlite3

DB_NAME = "books.db"

def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT,
            year INTEGER,
            isbn TEXT,
            pages INTEGER,
            pages_read INTEGER,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_book(title, author, genre, year, isbn, pages, pages_read, status):
    try:
        # Validate inputs
        year = int(year) if year else None
        pages = int(pages) if pages else None
        pages_read = int(pages_read) if pages_read else None

        # Check if year, pages, and pages_read are valid
        if year and (year < 1000 or year > 9999):
            raise ValueError("Invalid year entered.")
        if pages and pages < 1:
            raise ValueError("Invalid number of pages.")
        if pages_read and (pages_read < 0 or pages_read > pages):
            raise ValueError("Pages read cannot be greater than total pages.")

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(''' 
            INSERT INTO books (title, author, genre, year, isbn, pages, pages_read, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (title, author, genre, year, isbn, pages, pages_read, status))
        conn.commit()
        conn.close()
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Database Error: {e}")

def get_books(sort_by=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Default query
    query = "SELECT id, title, author, genre, year, status, isbn FROM books"
    
    # Add sorting if provided
    if sort_by:
        query += f" ORDER BY {sort_by}"
    
    cursor.execute(query)
    books = cursor.fetchall()
    conn.close()
    return books

def search_books(keyword):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, genre, year, status, isbn FROM books WHERE title LIKE ? OR author LIKE ?", 
                   ('%' + keyword + '%', '%' + keyword + '%'))
    books = cursor.fetchall()
    conn.close()
    return books

def delete_book(book_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

def update_book(book_id, title, author, genre, year, isbn, pages, pages_read, status):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(''' 
        UPDATE books SET title=?, author=?, genre=?, year=?, isbn=?, pages=?, pages_read=?, status=? 
        WHERE id=?
    ''', (title, author, genre, year, isbn, pages, pages_read, status, book_id))
    conn.commit()
    conn.close()
