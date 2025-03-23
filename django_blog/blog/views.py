from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, RegisterForm
from django.contrib.auth import login, logout
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView

# Create your views here.
class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class BlogCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('home/')

class BLogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('home/')

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home/')


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
    posts  = Post.objects.all()
    return render(request, 'blog/home.html', {"posts": posts})

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
            form.save(user=request.user)
            return redirect('/home')
    else:
        form = PostForm()
    return render(request, 'blog/post.html', {"form": form})