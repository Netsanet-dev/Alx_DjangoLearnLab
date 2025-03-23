from django.shortcuts import render, redirect
from .forms import PostForm, RegisterForm
from django.contrib.auth import login, logout

# Create your views here.
def register(request):
    if request.method == "POST":
        form = request.POST
        if form.is_valid():
            user = RegisterForm(request.user)
            login(request, user)
            return redirect("/home")
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {"form": form})

def home(request):
    return render(request, 'blog/home.html')

def profile(request):
    return render(request, 'blog/profile.html')

def log_in(request):
    return render(request, 'registration/login.html')

def log_out(request):
    logout(request.user)
    return render(request, 'registration/logout.html')

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