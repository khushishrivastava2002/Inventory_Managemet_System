from rest_framework import viewsets
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.

class MenViewSet(viewsets.ModelViewSet):
    queryset = men.objects.all()
    serializer_class = MenSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WomenViewSet(viewsets.ModelViewSet):
    queryset = women.objects.all()
    serializer_class = womenSerializer

class MainViewSet(viewsets.ModelViewSet):
    queryset = main.objects.all()
    serializer_class = mainSerializer