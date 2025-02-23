from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import list_books, LibraryDetailView, login_view

urlpatterns = [
    path('books/', list_books, name='books'),
    path('library/<int:pk>', LibraryDetailView.as_view(), name="Library"),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html', name='logout')),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html', name='login'))
]

