from rest_framework import generics, permissions, authentication
from rest_framework.viewsets import ModelViewSet
from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class PokemonDestroyAPIView(generics.DestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class PokemonUpdateAPIView(generics.UpdateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class PokemonViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    lookup_field = 'dexNumber'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]