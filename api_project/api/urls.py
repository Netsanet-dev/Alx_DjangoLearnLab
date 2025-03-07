from django.urls import path
from . import views

urlpatterns = [
    path('api/player', views.PlayerListCreateApiView.as_view(), name='player')
]
