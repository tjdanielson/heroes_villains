
from django.db.models import Count
from rest_framework.decorators import APIView
from super_types.models import SuperType
from .serializers import SuperSerializer
from .models import Power, Super
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SuperList(APIView):

    def get(self, request):
        type_param = request.query_params.get('type')
        supers = Super.objects.all()
        custom_response = {}
        super_types = SuperType.objects.all()
        if type_param:
            supers = supers.filter(super_type__type=type_param)
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            for super_type in super_types:
                heroes = Super.objects.filter(super_type_id=1)
                hero_serializer = SuperSerializer(heroes, many=True)
                villians = Super.objects.filter(super_type_id=2)
                villian_serializer = SuperSerializer(villians, many=True)
                custom_response = {
                    "heroes": hero_serializer.data,
                    "villains": villian_serializer.data
                }
            return Response(custom_response, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SuperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SuperDetail(APIView):

    def get_object(self, pk):
        try:
            return Super.objects.get(pk=pk)
        except Super.DoesNotExist:
            raise Http404

    def get_power(self, pk):
        try:
            return Power.objects.get(pk=pk)
        except Power.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        super = self.get_object(pk)
        serializer = SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        super = self.get_object(pk)
        serializer = SuperSerializer(super, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        super = self.get_object(pk)
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk, pk2):
        super = self.get_object(pk)
        power = self.get_power(pk2)
        super.powers.add(power)
        serializer = SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SuperFight(APIView):

    def get_super(self, super):
        try:
            return Super.objects.get(name=super)
        except Super.DoesNotExist:
            raise Http404
    
    def determine_valid_fight(self, super_one, super_two):
        super_one_type = super_one.super_type
        super_two_type = super_two.super_type
        if super_one_type == super_two_type:
            return False
        else:
            return True

    def get_power_count(self, super):
        count_of_powers = Super.objects.annotate(powers_count=Count('powers')).get(id=super.id)
        count = count_of_powers.powers_count
        return count

    def get(self, request, super_one, super_two):
        super_one = self.get_super(super_one)
        super_two = self.get_super(super_two)
        valid_fight = self.determine_valid_fight(super_one, super_two)
        if valid_fight == False:
            if super_one.super_type_id == 1:
                return Response(f'The supers you chose are both {super_one.super_type.type}s. Legally, they are not allowed to fight each other! Try again...', status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
            else:
                return Response(f'The supers you chose are both {super_one.super_type.type}s. Villains get too unruly and we refuse to host villain on villain battles until they promise to clean up after themseles.', status=status.HTTP_418_IM_A_TEAPOT)
        super_one_powers = self.get_power_count(super_one)
        super_two_powers = self.get_power_count(super_two)
        if super_one_powers == super_two_powers:
            custom_response = "IT IS A DRAW!"
        elif super_one_powers > super_two_powers:
            winner_serializer = SuperSerializer(super_one)
            loser_serializer = SuperSerializer(super_two)
        else:
            winner_serializer = SuperSerializer(super_two)
            loser_serializer = SuperSerializer(super_one)
        custom_response = {
            "WINNER": winner_serializer.data,
            "LOSER": loser_serializer.data
        }
        return Response(custom_response, status=status.HTTP_200_OK)
        





    

