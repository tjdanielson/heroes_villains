from django.http import Http404
from rest_framework.decorators import APIView
from .serializers import SuperTypeSerializer
from .models import SuperType
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SuperTypeList(APIView):

    def get(self, request):
        super_types = SuperType.objects.all()
        serializer = SuperTypeSerializer(super_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SuperTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SuperTypeDetails(APIView):

    def get_object(self, pk):
        try:
            return SuperType.objects.get(pk=pk)
        except SuperType.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        super_type = self.get_object(pk)
        serializer = SuperTypeSerializer(super_type)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        super_type = self.get_object(pk)
        serializer = SuperTypeSerializer(super_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        super_type = self.get_object(pk)
        super_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

