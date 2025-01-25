import sys
from PyQt5.QtWidgets import QApplication
from gui import BookCatalogApp
from db import initialize_db

if __name__ == "__main__":
    initialize_db()
    app = QApplication(sys.argv)
    window = BookCatalogApp()
    window.show()
    sys.exit(app.exec_())
