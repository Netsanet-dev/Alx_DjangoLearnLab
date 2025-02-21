from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book

# Create your views here.
def books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryBooks(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'
    
