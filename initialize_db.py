import sqlite3

def initialize_database():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Create books table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        copies INTEGER NOT NULL
    )
    ''')

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        borrowed_book_id INTEGER,
        FOREIGN KEY (borrowed_book_id) REFERENCES books (id)
    )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    initialize_database()
