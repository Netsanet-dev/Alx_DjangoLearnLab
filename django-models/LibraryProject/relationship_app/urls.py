from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

urlpatterns = [
    path('books/', views.list_books, name='books'),
    path('library/<int:pk>', views.LibraryDetailView.as_view(), name="Library"),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html', name='logout')),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html', name='login')),
    path('register/',views.register,name='register')
]

