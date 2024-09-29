from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_view(request):
    """A basic function view returning a greeting message."""
    return HttpResponse("Hello, World!")

from django.shortcuts import render
from .models import Book

def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'books/book_list.html', context)

#Checkers

#Checks for the “Utilize Django’s built-in views and forms for handling user authentication. You will need to create views for user login, logout, and registration.” task

from django.contrib.auth import login", "from django.contrib.auth.forms import UserCreationForm