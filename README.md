# Library Manager

A small campus library program. It stores books, magazines and DVDs, lets members borrow and return them, and raises a clear error when an action is not allowed.

Run it with:

```
python main.py
```

## Reflection

**Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?**

LibraryItem is abstract because every item shares title, id and availability, but each type charges a different late fee. The parent declares `late_fee()` with `@abstractmethod` and does not pick a rate, so a child class is not finished until it writes its own version. If DVD forgets `late_fee()`, DVD stays abstract too, and `DVD(...)` raises `TypeError` instead of creating an object.

**What happens when you read item.__available from outside the class, and why do we use is_available() instead?**

Reading `item.__available` from outside the class raises `AttributeError`. Python renames a `__` attribute inside the class (name mangling), so the real flag is not visible under that name and outside code cannot change it by accident. `is_available()` is the public method that reads the flag for us, which keeps the availability private and still lets the rest of the program check it.

**What is the difference between LibraryItem.total_items and self.title?**

`LibraryItem.total_items` is a class attribute: one shared counter that goes up by 1 each time any book, magazine or DVD is created. `self.title` is an instance attribute: each object stores its own title, so two items can have different titles. Changing one item's title does not change `total_items` or any other item's title.
