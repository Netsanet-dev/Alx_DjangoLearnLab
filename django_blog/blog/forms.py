from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.author = user
        if commit:
            instance.save()
        return instance
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']