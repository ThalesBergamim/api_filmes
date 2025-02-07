from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorCreateListView(generics.ListCreateAPIView):
    queryset=Actor.objects.all()
    serializer_class= ActorSerializer
    permission_classes = (IsAuthenticated,)

class ActorRetrieveUpdateDestroiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated,)
    