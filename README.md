# 📚 Library Management System (Python + SQLite)

A simple command-line **Library Management System** built with Python and SQLite. This project allows users to add, view, and issue books, with persistent data storage using a local database.

---

## 🚀 Features

- Add new books with title, author, and number of copies
- View all available books
- Issue a book to a user (reduces available copies)
- Simple database schema with `books` and `users` tables
- Data persistence using SQLite (`library.db`)

---

## 🗂️ Project Structure

library-management/
├── library.py # Main program logic
├── initialize_db.py # Initializes the database tables
├── library.db # SQLite database (auto-created)
└── README.md


---

## 🛠️ Requirements

- Python 3.x

No external libraries are required — uses Python’s built-in `sqlite3`.

---

## 📦 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/library-management.git
cd library-management

#Initialize the database
python initialize_db.py

#Run the main program
python library.py
```

---

📄 License

This project is open source and available under the MIT License.
