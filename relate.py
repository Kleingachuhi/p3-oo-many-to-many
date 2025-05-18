#  Handling many to many relationships. We have with intermediary class and without intermediary class.

class Parent:
    all = []

    def __init__(self, name, children=None):
        self.name = name
        self._children = []
        if children:
            for child in children:
                self.add_child(child)
        Parent.all.append(self)

    def children(self):
        return self._children

    def add_child(self, child):
        if isinstance(child, Child):
            self._children.append(child)
        else:
            raise ValueError("Child must be an instance of the Child class.")

class Child:
    def __init__(self, name):
        self.name = name

    def parents(self):
        return [parent for parent in Parent.all if self in parent.children()]

    def add_parent(self, parent):
        if isinstance(parent, Parent):
            parent.add_child(self)
        else:
            raise ValueError("Parent must be an instance of the Parent class.")


class Book:
    all_books = []
    def __init__(self, title, price):
        self.title = title
        self.price = price
        Book.all_books.append(self)
    def __str__(self):
        return  str(self.title)
# class Author:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
my_book1 = Book("Harry Potter", 789)
my_library = Book("The hobbit", 900)
for book in Book.all_books:
    print(f" {book} is this price {book.price}.")
    