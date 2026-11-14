# main.py
from models import Book, Magazine, DVD, Member, LibraryItem

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Campus Weekly", 2, 14)
dvd = DVD("Intro to OOP", 3, 90)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    print("Alice's books:", alice.borrowed_titles())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

# 2. Borrow-limit error (Bob may hold only 1 item)
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # should fail: limit reached
except ValueError as e:
    print("Could not borrow:", e)

# 3. Returning an item this member never borrowed
try:
    alice.return_item(dvd)
except ValueError as e:
    print("Could not return:", e)

# 4. A valid return gives back the late fee
try:
    fee = alice.return_item(book, days_late=3)
    print("Alice returned the book. Late fee: Rs", fee)
    print("Alice's books:", alice.borrowed_titles())
    print("Book available?", book.is_available())
except ValueError as e:
    print("Could not return:", e)

# 5. Polymorphism: one loop, no type checks
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 6. Encapsulation: the private flag is hidden; use the method
try:
    print(book.__available)
except AttributeError as e:
    print("Private attribute is hidden:", e)
print("Book available?", book.is_available())

# 7. Class attribute shared by all objects
print("Total items created:", LibraryItem.total_items)
