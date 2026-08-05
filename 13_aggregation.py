#It is a relationship where one class contains an object of another class
#Both objects can exist independently
class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
    def add_books(self,book):
        self.books.append(book)
    def list_books(self):
        return [f"{book.name} by {book.author}"for book in self.books]
class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author
library=Library("The Book Shelf")
book1=Book("Harry Potter","J.K. Rowling")
book2=Book("The Hamlet","William Shakespeare")
library.add_books(book1)
library.add_books(book2)
print(library.name)
for book in library.list_books():
    print(book)