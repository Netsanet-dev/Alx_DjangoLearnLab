from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, SignUpView

urlpatterns = [
    path('books/', list_books, name='books'),
    path('library/<int:pk>', LibraryDetailView.as_view(), name="Library"),
    path('', LoginView.as_view(template_name='relationship_app/login.html'), name='login' ),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', SignUpView.as_view(), name='register')
]

