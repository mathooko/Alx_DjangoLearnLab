from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name= models.CharField(max_length=200)
class Book:
    title=models.CharField(max_length=200)
    author=models.ForeignKey(Author)
class Library:
    name=models.CharField(max_length=200)
    books=models.ManyToManyField(Book)
class Librarian:
    name=models.CharField(max_length=200)
    library=models.OneToOneField(Library)

         
    return self.name