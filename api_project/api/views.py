from .serializers import PlayerSerializer
from .models import Player
from rest_framework import generics
# Create your views here.

class PlayerListCreateApiView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer