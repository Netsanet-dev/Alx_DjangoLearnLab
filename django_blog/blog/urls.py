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
    path('post/new/', views.BlogCreateView.as_view(), name="create-posts"),
    path('posts/<int:pk>/', views.BlogDetailView.as_view(), name="detail-posts"),
    path('post/<int:pk>/update/', views.BLogUpdateView.as_view(), name="update-posts"),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name="delete-posts"),

    # Class View for comment
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name="comment-create"),
    path('post/<int:pk>/comments/new/', views.BlogCreateView.as_view(), name="comment-create"),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name="delete-comment"),

    # Tag
    path("tags/<slug:tag_slug>/", views.PostByTagListView.as_view(), name="tag-list")
]
