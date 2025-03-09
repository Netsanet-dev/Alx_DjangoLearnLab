from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet, TokenView
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books', BookList.as_view(), name='book-list'),
    path('user-token/', obtain_auth_token, name='user-token'),
    path('token-view', TokenView.as_view(), name='token-view'),
    path('', include(router.urls))
]
