import sqlite3

def main_menu():
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. View Books")
    print("3. Issue a Book")
    print("4. Exit")
    return input("Enter your choice: ")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    copies = int(input("Enter number of copies: "))

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, copies) VALUES (?, ?, ?)", (title, author, copies))
    conn.commit()
    conn.close()
    print("Book added successfully!")

def view_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    print("\nAvailable Books:")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Copies: {book[3]}")
    conn.close()

def issue_book():
    user_name = input("Enter your name: ")
    book_id = int(input("Enter book ID to borrow: "))

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Check if book is available
    cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()

    if book and book[3] > 0:
        cursor.execute("UPDATE books SET copies = copies - 1 WHERE id = ?", (book_id,))
        cursor.execute("INSERT INTO users (name, borrowed_book_id) VALUES (?, ?)", (user_name, book_id))
        conn.commit()
        print(f"{user_name} successfully borrowed '{book[1]}'.")
    else:
        print("Book not available.")
    
    conn.close()

if __name__ == "__main__":
    while True:
        choice = main_menu()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
