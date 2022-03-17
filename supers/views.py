from rest_framework.decorators import APIView
from .serializers import SuperSerializer
from .models import Super
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SuperList(APIView):

    def get(self, request):
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

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

    def get(self, request, pk):
        super = self.get_object(pk)
        serializer = SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

