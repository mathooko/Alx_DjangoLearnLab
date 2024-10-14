from django.contrib import admin
from .models import Book

# Register your models here.
"register", "admin.ModelAdmin"
"list_filter", "author", "publication_year"
"search_fields", "title"

#Check for Custom User Admin Registration:
   
 - LibraryProject/bookshelf/admin.py doesn't contain: ["admin.site.register(CustomUser, CustomUserAdmin)"]