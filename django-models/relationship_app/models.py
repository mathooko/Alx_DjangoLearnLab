from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name= models.CharField(max_length=200)
    def __str__(self):# String representations
            # Without this, we see the object representation in memory
            return self.name
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(Author)
class Library(models.Model):
    name=models.CharField(max_length=200)
    books=models.ManyToManyField(Book)
class Librarian(models.Model):
    name=models.CharField(max_length=200)
    library=models.OneToOneField(Library)


    "class UserProfile(models.Model):", "Admin", "Member"
    ["class Meta", "permissions"]
    "can_add_book", "can_change_book", "can_delete_book"

    # Check for models.py File Existence and Custom Permissions Definition:
    "class Book(models.Model):", "can_create", "can_delete"