from rest_framework import generics
from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer
from .models import Ability
from .serializers import AbilitySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class AbilityRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer

class AbilityListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer

class AbilityDestroyAPIView(generics.DestroyAPIView):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer

class AbilityUpdateAPIView(generics.UpdateAPIView):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer

@api_view(['GET'])
def api_abilities(request):
    instanceAbility = Ability.objects.all().order_by('?').first()

    aData = {}
    if instanceAbility:
        aData = AbilitySerializer(instanceAbility).data['aName']

    instancePokemon = Pokemon.objects.all().filter(ability=aData)

    pData = []
    if instancePokemon:
        for pokemon in instancePokemon:
            pData.append(PokemonSerializer(pokemon).data)
        

    return Response(pData)