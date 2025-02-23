from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Library, Book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# user = User.objects.create_user('Nesanet', 'Nets@gmail.com', 'pass123')
# user = User.objects.get(username='Nesanet')
# Create your views here.
class SignUpView(CreateView):
   form_class = UserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'relationship_app/register.html'

@login_required
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'
    
