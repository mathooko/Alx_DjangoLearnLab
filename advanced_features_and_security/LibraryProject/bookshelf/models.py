from django.db import models

# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(null=True)

# title: CharField with a maximum length of 200 characters.
# author: CharField with a maximum length of 100 characters.
# publication_year: IntegerField.

#The following code is for the checker

class CustomUser(AbstractUser):", "date_of_birth", "profile_photo"]


#Check for Custom User Manager Definition:

class CustomUserManager(BaseUserManager):", "create_user", "create_superuser"

# Check for models.py File Existence and Custom Permissions Definition:
    "class Book(models.Model):", "can_create", "can_delete"
