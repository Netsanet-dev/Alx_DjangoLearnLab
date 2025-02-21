from django.shortcuts import render
from django.views.generic import ListView
from .models import Author, Book, Librarian, Library

# Create your views here.
def books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)

class LibraryBooks(ListView):
    model = Library
    context_object_name = 'library'
    template_name = 'books/library_detail.html'
    
