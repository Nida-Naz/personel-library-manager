import json
import os

data_file = "library.txt"

# Load library from file (if exists)
def load_library():
    if os.path.exists(data_file):  # Corrected 'exists'
        with open(data_file, 'r') as file:
            return json.load(file)
    return []   # Corrected placement of return

# Save library to file
def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file, indent=4)

# Add a book to the library
def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")
    genre = input("Enter genre: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"

    new_book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Genre": genre,
        "Read": read
    }

    library.append(new_book)
    save_library(library)
    print(f'✅ Book "{title}" added successfully!')

# Remove a book by title
def remove_book(library):
    title = input("Enter the title of the book to remove: ").lower()
    initial_length = len(library)
    library = [book for book in library if book["Title"].lower() != title]

    if len(library) < initial_length:
        save_library(library)
        print(f'✅ Book "{title}" removed successfully.')
    else:
        print(f'❌ Book "{title}" not found in the library.')

# Search for books by title or author
def search_book(library):
    choice = input("Search by: 1. Title 2. Author\nEnter choice: ")
    search_term = input("Enter search term: ").lower()

    if choice == "1":
        result = [book for book in library if search_term in book["Title"].lower()]
    elif choice == "2":
        result = [book for book in library if search_term in book["Author"].lower()]
    else:
        print("❌ Invalid search option!")
        return

    if result:
        for book in result:
            status = 'Read' if book['Read'] else 'Unread'
            print(f"{book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} [{status}]")
    else:
        print(f"No books found matching '{search_term}'.")

# Display all books
def display_all_books(library):
    if library:
        for book in library:
            status = 'Read' if book['Read'] else 'Unread'
            print(f"{book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} [{status}]")
    else:
        print("The library is empty.")

# Display statistics
def display_status(library):
    total_books = len(library)
    read_books = len([book for book in library if book["Read"]])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"📚 Total books: {total_books}")
    print(f"✅ Percentage read: {percentage_read:.2f}%")

# Menu system
def main():
    library = load_library()
    while True:
        print("\n📖 Library Menu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_status(library)
        elif choice == "6":
            save_library(library)
            print("📂 Library saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()

