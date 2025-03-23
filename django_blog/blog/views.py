from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, RegisterForm
from django.contrib.auth import login, logout
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView

# Create your views here.
class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post

class BlogCreateView(CreateView):
    pass

class BLogUpdateView(UpdateView):
    pass

class BlogDeleteView(DeleteView):
    pass


def register(request):
    if request.method == "POST":
        form = request.POST
        if form.is_valid():
            user = RegisterForm(request.user)
            login(request, user)
            return redirect("/home")
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {"form": form})

def home(request):
    return render(request, 'blog/home.html')

def profile(request):
    return render(request, 'blog/profile.html')

def log_in(request):
    return render(request, 'blog/login.html')

def log_out(request):
    logout(request.user)
    return render(request, 'blog/logout.html')

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.author = request.user
            user.save()
            return redirect('/home')
    else:
        form = PostForm()
    return render(request, 'blog/post.html', {"form": form})