from .serializers import BookSerializer
from .models import Book
from rest_framework import generics
# Create your views here.

class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer