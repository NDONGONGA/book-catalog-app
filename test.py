books = [ ]
def add_book():
    print(f"Book '{name}' Added Successfully")

def search_book():
    name = input("Enter Book Name :")
    for book in books:
        if book["Name"].lower() == name.lower():
            print(f"Found: {book}")
            return
    print("Book Not Found")
def mark_read():
    name = input("Enter Book Name :")
    for book in books:
        if book["Name"].lower() == name.lower():
            book["status"] = "Read"
            print(f"Book '{book["Name"]}' Mark Readed Successfully" )
            return
    print("Book Not Found")
def delete_book():
    name = input("Enter Book Name :")
    for book in books:
        if book["Name"].lower() == name.lower():
            books.remove(book)
            print(f"Book '{book["Name"]}' Deleted Successfully")
            return
    print("Book Not Found")
def show_book():
    if not books:
        print("No books in the library.")
        return
    for book in books:
        print(f"{book['Name']} by {book['Author']} ({book['Year']}) - {book['status']}")

while True:
    print("\nMenu:")
    print("1: Add Book")
    print("2: Search Book")
    print("3: Mark Book as Read")
    print("4: Delete Book")
    print("5: Show All Books")
    print("0: Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        mark_read()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        show_book()
    elif choice == "0":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")