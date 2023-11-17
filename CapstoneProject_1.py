# Name: Batari Raisya Aviani
# Class JCDSOL-012 (C)

# Library Management - Capstone Project (Module 01)
# For Librarian

library = {
    'ENG-001': {'Title': 'Fourth Wing', 'Author': 'Rebecca Yarros', 'Quantity': 1, 'Genre': 'Fantasy', 'Status': 'Available'},
    'ENG-002': {'Title': 'Once Upon A Broken Heart', 'Author': 'Stephanie Garber', 'Quantity': 1, 'Genre': 'Fantasy', 'Status': 'Available'},
    'ENG-003': {'Title': 'Beach Read', 'Author': 'Emily Henry', 'Quantity': 1, 'Genre': 'Romance', 'Status': 'Available'},
    'INA-001': {'Title': 'Winter in Tokyo', 'Author': 'Ilana Tan', 'Quantity': 1, 'Genre': 'Romance', 'Status': 'Available'},
    'INA-002': {'Title': 'The Architecture of Love', 'Author': 'Ika Natassa', 'Quantity': 1, 'Genre': 'Romance', 'Status': 'Available'}
}

borrowed_books = []

def lend_book():
    book_id = input("\nEnter Book ID to lend: ").upper()
    if book_id in library and library[book_id]['Quantity'] > 0:
        reader_name = input("Enter the reader's name: ").strip().title()

        if reader_name:
            library[book_id]['Reader'] = reader_name
            library[book_id]['Quantity'] -= 1

            if library[book_id]['Quantity'] == 0:
                library[book_id]['Status'] = "Out of Stock"

            print(f"\nBook lent successfully to {reader_name}. Don't forget to remind {reader_name} to return it on time!")
            borrowed_books.append({'Book ID': book_id, 'Reader': reader_name})
        else:
            print("Name cannot be empty. Please input a valid name.")
    elif book_id in library and library[book_id]['Quantity'] == 0:
        print("\nSorry, the book is out of stock. Check again later.")
    else:
        print("\nBook ID not found. Please enter the correct Book ID or add a book to the library by selecting '5'.")

def return_book():
    book_id = input("\nEnter Book ID to return: ").upper()
    if book_id in library and library[book_id]['Quantity'] < 1:
        reader_name = input("Enter the reader's name: ").strip().title()

        if library[book_id].get('Reader', '').title() == reader_name:
            library[book_id]['Quantity'] += 1

            if library[book_id]['Quantity'] > 0:
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
    while True:
        if library:
            print("\nBooks in Purwadhika Library:")
            print("-" * 110)
            print(f"| {'Book ID':^10} | {'Title':^27} | {'Author':^20} | {'Quantity':^10} | {'Genre':^10} | {'Status':^14} |")
            print("-" * 110)

            for book_id, book_info in library.items():
                print(f"| {book_id:^10} | {book_info['Title']:^27} | {book_info['Author']:^20} | {book_info['Quantity']:^10} | {book_info['Genre']:^10} | {book_info['Status']:^14} |")

            print("-" * 110)
            print("1. Edit a book")
            print("2. Add a book")
            print("3. Delete a book")
            print("4. Return to main menu")
            choice = input("Select an option (1/2/3/4): ")

            if choice == "1":
                edit_book_id = input("Enter the Book ID you want to edit: ").upper()
                edit_book(edit_book_id)
            elif choice == "2":
                add_book()
            elif choice == "3":
                delete_book()
            elif choice == "4":
                break
            else:
                print("Invalid option. Please select a valid option.")

        else:
            print("\nLibrary is currently empty.")
            print("\nYou can add new books to the library by selecting '5'.")
            break

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
                if new_quantity == 0 or new_quantity == 1:
                    library[book_id]['Quantity'] = new_quantity
                    if new_quantity == 0:
                        library[book_id]['Status'] = "Out of Stock"
                    print("\nQuantity updated successfully.")
                    break
                else:
                    print("Quantity must be 0 or 1. Please enter a valid quantity.")
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
    while True:
        if borrowed_books:
            print("\nBooks currently borrowed:")
            print("-" * 67)
            print(f"| {'Book ID':^10} | {'Title':^27} | {'Borrowed by':^20} |")
            print("-" * 67)

            for book in borrowed_books:
                book_id = book.get('Book ID', '')
                title = library.get(book_id, {}).get('Title')
                reader = book.get('Reader')

                print(f"| {book_id:^10} | {title:^27} | {reader:^20} |")

            print("-" * 67)
            print("1. Return a book")
            print("2. Return to main menu")
            choice = input("Select an option (1/2): ")

            if choice == "1":
                return_book()
            elif choice == "2":
                break
            else:
                print("Invalid option. Please select a valid option")
    
        else:
            print("\nNo books are currently borrowed.")
            break

def add_book():
    book_id = input("\nEnter Book ID: ").upper()
    title = input("Enter Book Title: ").title()
    author = input("Enter Author: ").title()
    
    while True:
        quantity = int(input("Enter Quantity: "))
        if quantity == 0 or quantity == 1:
            break
        else:
            print("Quantity must be 0 or 1. Please enter a valid quantity.")
    if quantity == 0:
        status = "Out of Stock"
    else:
        status = "Available"
    genre = input("Enter Genre: ").title()
    confirmation = input(f"\nAre you sure you want to add '{title}' to the library? (Y/N): ").strip().lower()

    if confirmation == 'y':
        library[book_id] = {'Title': title, 'Author': author, 'Quantity': quantity, 'Genre': genre, 'Status': status}
        print("\nBook added successfully. It is now available for readers.")
    else:
        print("\nBook addition cancelled.")

def delete_book():
    book_id = input("\nEnter Book ID to delete: ").upper()
    if book_id in library:
        confirmation = input(f"\nAre you sure you want to delete '{library[book_id]['Title']}' from the library? (Y/N): ").strip().lower()
        
        if confirmation == 'y':
            del library[book_id]
            print("\nBook deleted successfully. It is now removed from the library.")
        else:
            print("\nBook deletion cancelled.")
    else:
        print("\nBook ID not found. Please enter the correct Book ID.")

while True:
    print("\n+" + "-" * 46 + "+")
    print("| Welcome to Purwadhika Library Management App |")
    print("+" + "-" * 46 + "+")
    print("\nYou can add, delete, and manage books in the library")
    print("-" * 52)
    print("1. Lend Book")
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
