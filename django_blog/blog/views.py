from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Post, Comment, Tag
from .forms import PostForm, RegisterForm
from django.contrib.auth import login, logout
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.db.models import Q
# Create your views here.
class BlogListView(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'

class BlogDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class BlogCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('home/')

class BLogUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('home/')

class BlogDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home/')

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'blog/comment_create.html'
    success_url = reverse_lazy('/home')

class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'blog/comment_update.html'
    success_url = reverse_lazy('/home')

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'
    success_url = reverse_lazy('/home')


@login_required(login_url='login/')
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

@login_required(login_url='login/')
def home(request):
    posts  = Post.objects.all()
    return render(request, 'blog/home.html', {"posts": posts})

@login_required(login_url='login/')
def profile(request):
    return render(request, 'blog/profile.html')

def log_in(request):
    return render(request, 'blog/login.html')

@login_required(login_url='login/')
def log_out(request):
    logout(request.user)
    return render(request, 'blog/logout.html')

@login_required(login_url='login/')
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('/home')
    else:
        form = PostForm()
    return render(request, 'blog/post.html', {"form": form})

class PostByTagListView(ListView):
    template_name = 'search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
            ).distinct()
        return Post.objects.none()  # Return empty queryset if no query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

class PostsByTagView(ListView):
    template_name = 'tag_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        return Post.objects.filter(tags__name=tag_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs['tag_name']
        return context