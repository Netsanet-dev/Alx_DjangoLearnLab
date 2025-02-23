from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Library, Book
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# user = User.objects.create_user("Netsanet", "Nets@gmail.com", "pass4321")

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("relationship_app/list_books.html")
    return render(request, "relationship_app/login.html")


def logout_view(request):
    pass

def register(request):
    return render(request, 'relationshipapp/register.html')


@login_required
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'
    
