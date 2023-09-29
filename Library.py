class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store book information
        self.users = {}  # Dictionary to store user information

    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            self.books[book_id] = {'title': title, 'author': author, 'available': True}
            print(f"Book '{title}' by {author} added to the library.")
        else:
            print(f"Book with ID {book_id} already exists in the library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print(f"Book with ID {book_id} removed from the library.")
        else:
            print(f"Book with ID {book_id} not found in the library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book_id, book_info in self.books.items():
                status = "Available" if book_info['available'] else "Not available"
                print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Status: {status}")

    def add_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = {'name': name, 'books_checked_out': []}
            print(f"User '{name}' added to the library.")
        else:
            print(f"User with ID {user_id} already exists in the library.")

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            print(f"User with ID {user_id} removed from the library.")
        else:
            print(f"User with ID {user_id} not found in the library.")

    def list_users(self):
        if not self.users:
            print("No users in the library.")
        else:
            print("Users in the library:")
            for user_id, user_info in self.users.items():
                print(f"ID: {user_id}, Name: {user_info['name']}")

    def borrow_book(self, user_id, book_id):
        if user_id in self.users and book_id in self.books:
            if self.books[book_id]['available']:
                self.users[user_id]['books_checked_out'].append(book_id)
                self.books[book_id]['available'] = False
                print(f"User {self.users[user_id]['name']} has borrowed '{self.books[book_id]['title']}'.")
            else:
                print(f"Book '{self.books[book_id]['title']}' is not available.")
        else:
            print("User or book not found in the library.")

    def return_book(self, user_id, book_id):
        if user_id in self.users and book_id in self.books:
            if book_id in self.users[user_id]['books_checked_out']:
                self.users[user_id]['books_checked_out'].remove(book_id)
                self.books[book_id]['available'] = True
                print(f"User {self.users[user_id]['name']} has returned '{self.books[book_id]['title']}'.")
            else:
                print(f"User {self.users[user_id]['name']} does not have '{self.books[book_id]['title']}' checked out.")
        else:
            print("User or book not found in the library.")

if __name__ == "__main__":
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Add User")
        print("5. Remove User")
        print("6. List Users")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(book_id, title, author)
        elif choice == '2':
            book_id = input("Enter book ID to remove: ")
            library.remove_book(book_id)
        elif choice == '3':
            library.list_books()
        elif choice == '4':
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            library.add_user(user_id, name)
        elif choice == '5':
            user_id = input("Enter user ID to remove: ")
            library.remove_user(user_id)
        elif choice == '6':
            library.list_users()
        elif choice == '7':
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID to borrow: ")
            library.borrow_book(user_id, book_id)
        elif choice == '8':
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID to return: ")
            library.return_book(user_id, book_id)
        elif choice == '9':
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
