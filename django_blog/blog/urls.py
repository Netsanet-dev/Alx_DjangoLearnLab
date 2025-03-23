from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='logout'),
    path('login/', views.log_in, name='login'),
    path('post/', views.create_post, name='post'),
    path('profile/', views.profile, name='profile'),
    
    # Class Views
    path('posts/', views.BlogListView.as_view(), name='list-posts'),
    path('posts/new/', views.BlogCreateView.as_view(), name="create-posts"),
    path('posts/<int:pk>/', views.BlogDetailView.as_view(), name="detail-posts"),
    path('posts/<int:pk>/edit/', views.BLogUpdateView.as_view(), name="update-posts"),
    path('posts/<int:pk>/delete/', views.BlogDeleteView.as_view(), name="delete-posts")

]
