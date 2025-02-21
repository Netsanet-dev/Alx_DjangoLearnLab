from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books, name='books'),
    path('library/<int:pk>', views.LibraryBooks.as_view(), name="Library")
    
]
