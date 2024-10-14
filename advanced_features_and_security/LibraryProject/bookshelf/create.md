
from bookshelf.models import Book 

The book variable creates a book from the model in book class:

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)  

Save the book:

book.save

Here we are printing the title of the book:

print(book.title)

Output of the title:

1984


