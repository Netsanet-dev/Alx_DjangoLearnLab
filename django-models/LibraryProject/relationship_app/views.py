from django.shortcuts import render
from django.views.generic import ListView
from .models import Author, Book, Librarian, Library

# Create your views here.
def books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'list_books.html', context)

class LibraryBooks(ListView):
    model = Library
    context_object_name = 'library'
    template_name = 'library_detail.html'
    
