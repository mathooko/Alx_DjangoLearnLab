<!-- "book.delete", "from bookshelf.models import Book" -->
from bookshelf.models import Book 

book = Book.objects.delete(title)

