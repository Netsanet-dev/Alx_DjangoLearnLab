from django.urls import path
from . import views

urlpatterns = [
    path('api/books', views.BookListCreateApiView.as_view(), name='books'),
]
