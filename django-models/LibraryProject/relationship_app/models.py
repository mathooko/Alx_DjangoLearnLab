from django.db import models
from django.contrib.auth.models import User

class Author:
    name= models.CharField(max_length=200)
class Book:
    title=models.CharField(max_length=200)
    author=models.ForeignKey(Author)
class Library:
    name=models.CharField(max_length=200)
    books=models.ManyToManyField(Book)
class Librarin:
    name=models.CharField(max_length=200)
    library=models.OneToOneField(Library)

    