# Name: Batari Raisya Aviani
# Class JCDSOL-012 (C)

#Library Management - Capstone Project (Module 01)
#For Librarian

library = {
    'ENG-001': {'Title': 'Fourth Wing', 'Author': 'Rebecca Yarros', 'Quantity': 1, 'Genre': 'Fantasy', 'Status': 'Available'},
    'ENG-002': {'Title': 'Once Upon A Broken Heart', 'Author': 'Stephanie Garber', 'Quantity': 1, 'Genre': 'Fantasy', 'Status': 'Available'},
    'ENG-003': {'Title': 'Beach Read', 'Author': 'Emily Henry', 'Quantity': 5, 'Genre': 'Romance', 'Status': 'Available'},
}

borrowed_books = []

def lend_book():
    book_id = input("\nEnter Book ID to lend: ").upper()
    if book_id in library and library[book_id]['Quantity'] > 0:
        reader_name = input("Enter the reader's name: ").strip().title()
        library[book_id]['Reader'] = reader_name
        library[book_id]['Quantity'] -= 1
        library[book_id]['Status'] = "Borrowed"
        borrowed_books.append({'Book ID': book_id, 'Reader': reader_name})
        print(f"\nBook lent successfully to {reader_name}. Don't forget to remind {reader_name} to return it on time!")
    elif book_id in library and library[book_id]['Quantity'] == 0:
        print("\nSorry, the book is out of stock. Check again later.")
    else:
        print("\nBook ID not found. Please enter the correct Book ID or add a book to the library by selecting '5'.")

def return_book():
    book_id = input("\nEnter Book ID to return: ").upper()
    if book_id in library and library[book_id]['Status'] == "Borrowed":
        reader_name = input("Enter the reader's name: ").strip().title()
        if library[book_id].get('Reader', '').title() == reader_name:
            library[book_id]['Quantity'] += 1
            library[book_id]['Status'] = "Available"
            library[book_id]['Reader'] = ''
            for book in borrowed_books:
                if book['Book ID'] == book_id and book['Reader'] == reader_name:
                    borrowed_books.remove(book)
            print(f"\nBook has been returned successfully by {reader_name}.")
        else:
            print("\nIncorrect borrower name. Please enter the correct name or lend a book by selecting '1'.")
    elif book_id in library and library[book_id]['Status'] == "Available":
        print("\nThis book is not currently being borrowed. Please enter the correct Book ID or lend a book by selecting '1'.")
    else:
        print("\nBook ID not found. Please enter the correct Book ID or add a book to the library by selecting '5'.")

def view_books():
    if library:
        print("\nBooks in Purwadhika Library:")
        for book_id, book_info in library.items():
            print(f"\nBook ID: {book_id}")
            print(f"Title: {book_info['Title']}")
            print(f"Author: {book_info['Author']}")
            print(f"Quantity: {book_info['Quantity']}")
            print(f"Genre: {book_info['Genre']}")
            print(f"Status: {book_info['Status']}")
            print()

        edit_option = input("Do you want to edit a book? (Y/N): ").strip().lower()
        if edit_option == 'y':
            edit_book_id = input("Enter the Book ID you want to edit: ").upper()
            edit_book(edit_book_id)
    else:
        print("\nLibrary is currently empty.")
        print("\nYou can add new books to the library by selecting '1'.")

def edit_book(book_id):
    if book_id in library:
        print(f"\nEditing Book ID: {book_id}")
        print("1. Edit Title")
        print("2. Edit Author")
        print("3. Edit Quantity")
        print("4. Edit Genre")
        print("5. Go back to main menu")

        edit_choice = input("\nSelect an option (1/2/3/4/5): ")

        if edit_choice == '1':
            new_title = input("Enter the new title: ").title()
            library[book_id]['Title'] = new_title
            print("\nTitle updated successfully.")
        elif edit_choice == '2':
            new_author = input("Enter the new author: ").title()
            library[book_id]['Author'] = new_author
            print("\nAuthor updated successfully.")
        elif edit_choice == '3':
            while True:
                new_quantity = int(input("Enter the new quantity: "))
                if new_quantity > 0:
                    break
                else:
                    print("Quantity must be greater than 0. Please enter a valid quantity.")
            library[book_id]['Quantity'] = new_quantity
            print("\nQuantity updated successfully.")
        elif edit_choice == '4':
            new_genre = input("Enter the new genre: ").title()
            library[book_id]['Genre'] = new_genre
            print("\nGenre updated successfully.")
        elif edit_choice == '5':
            print("\nReturning to the main menu.")
        else:
            print("\nInvalid option. Returning to the main menu.")
    else:
        print("\nBook ID not found. Please enter the correct Book ID or add the book to the library by selecting '5'.")

def view_borrowed_books():
    if borrowed_books:
        print("\nBooks currently borrowed:")
        for book in borrowed_books:
            book_id = book.get('Book ID', '')
            title = library.get(book_id, {}).get('Title')
            reader = book.get('Reader')

            print(f"\nBook ID: {book_id}")
            print(f"Title: {title}")
            print(f"Borrowed by: {reader}")
            print()
    else:
        print("\nNo books are currently borrowed.")

def add_book():
    book_id = input("\nEnter Book ID: ").upper()
    title = input("Enter Book Title: ").title()
    author = input("Enter Author: ").title()
    
    while True:
        quantity = int(input("Enter Quantity: "))
        if quantity > 0:
            break
        else:
            print("Quantity must be greater than 0. Please enter a valid quantity.")

    genre = input("Enter Genre: ").title()
    status = "Available"
    confirmation = input(f"\nAre you sure you want to add '{title}' to the library? (Y/N): ").strip().lower()

    if confirmation == 'y':
        library[book_id] = {'Title': title, 'Author': author, 'Quantity': quantity, 'Genre': genre, 'Status': status}
        print("\nBook added successfully. It is now available for readers.")
    else:
        print("\nBook addition cancelled.")

def delete_book():
    book_id = input("\nEnter Book ID to delete: ").upper()
    if book_id in library:
        confirmation = input(f"\nAre you sure you want to delete '{library[book_id]['Title']}'from the library? (Y/N): ").strip().lower()
        if confirmation == 'y':
            del library[book_id]
            print("\nBook deleted successfully. It is now deleted from the library.")
        else:
            print("\nBook deletion cancelled.")
    else:
        print("\nBook ID not found. Please enter the correct Book ID.")

while True:
    print("\n--Welcome to Purwadhika Library Management App--")
    print("\nYou can add, delete, and manage books in the library.")
    print("\n1. Lend Book")
    print("2. Mark Book as Returned")
    print("3. View Library")
    print("4. View Borrowed Books")
    print("5. Add New Book")
    print("6. Delete Books")
    print("7. Exit")
    choice = input("\nSelect an option (1/2/3/4/5/6/7): ")

    if choice == '1':
        lend_book()
    elif choice == '2':
        return_book()
    elif choice == '3':
        view_books()
    elif choice == '4':
        view_borrowed_books()
    elif choice == '5':
        add_book()
    elif choice == '6':
        delete_book()
    elif choice == '7':
        print("\nThank you for managing the Purwadhika Library. See you soon!")
        break
    else:
        print("\nInvalid option. Please select a valid option.")
