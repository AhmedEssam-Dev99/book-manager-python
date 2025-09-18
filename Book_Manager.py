import json
import os

# 📁 File to store books
BOOKS_FILE = "books.json"

# 📥 Load books from JSON file
def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []  # Return empty list if file doesn't exist
    with open(BOOKS_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print("⚠️  books.json is corrupted. Starting fresh.")
            return []

# 📤 Save books to JSON file
def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4, ensure_ascii=False)

# ➕ Add a new book
def add_book(books):
    print("\n--- 📖 Add New Book ---")
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    year = input("Enter year: ").strip()
    genre = input("Enter genre (optional): ").strip()

    if not title or not author:
        print("❌ Title and author are required!")
        return

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre if genre else "N/A"
    }

    books.append(new_book)
    save_books(books)
    print("✅ Book added successfully!")

# 👀 View all books
def view_books(books):
    print("\n--- 📚 Your Library ---")
    if not books:
        print("📭 No books yet. Add some!")
        return

    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']}")

# 🔍 Search books by title or author
def search_books(books):
    print("\n--- 🔍 Search Books ---")
    query = input("Enter title or author to search: ").lower().strip()
    if not query:
        print("❌ Please enter a search term.")
        return

    results = [
        book for book in books
        if query in book['title'].lower() or query in book['author'].lower()
    ]

    if results:
        print(f"\n✅ Found {len(results)} result(s):")
        for i, book in enumerate(results, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']}")
    else:
        print("📭 No books match your search.")

# ❌ Delete a book
def delete_book(books):
    print("\n--- ❌ Delete Book ---")
    view_books(books)
    if not books:
        return

    try:
        index = int(input("\nEnter book number to delete: ")) - 1
        if 0 <= index < len(books):
            deleted = books.pop(index)
            save_books(books)
            print(f"✅ Deleted: {deleted['title']} by {deleted['author']}")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# 🎮 Main menu
def main():
    books = load_books()
    print("👋 Welcome to Ahmed’s Book Manager!")

    while True:
        print("\n--- 📖 MAIN MENU ---")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Books")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_books(books)
        elif choice == "4":
            delete_book(books)
        elif choice == "5":
            print("👋 Goodbye! Happy reading!")
            break
        else:
            print("❌ Invalid option. Try again.")

# 🚀 Run the app
if __name__ == "__main__":
    main()