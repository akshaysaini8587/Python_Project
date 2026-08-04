library = {}

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    library[book_id] = {
        "Title": title,
        "Author": author,
        "Status": "Available"
    }

    print("Book Added Successfully!\n")

def view_books():
    if not library:
        print("No Books Available.\n")
        return

    for book_id, details in library.items():
        print(f"\nBook ID : {book_id}")
        print(f"Title   : {details['Title']}")
        print(f"Author  : {details['Author']}")
        print(f"Status  : {details['Status']}")

def issue_book():
    book_id = input("Enter Book ID: ")

    if book_id in library:
        if library[book_id]["Status"] == "Available":
            library[book_id]["Status"] = "Issued"
            print("Book Issued Successfully.")
        else:
            print("Book Already Issued.")
    else:
        print("Book Not Found.")

def return_book():
    book_id = input("Enter Book ID: ")

    if book_id in library:
        library[book_id]["Status"] = "Available"
        print("Book Returned Successfully.")
    else:
        print("Book Not Found.")

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")