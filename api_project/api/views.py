from h11 import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class TokenView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Hello'})

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

