from rest_framework import viewsets
from .serializers import *


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StatusViewSets(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ClientsViewSets(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class FlatsViewSets(viewsets.ModelViewSet):
    queryset = Flats.objects.all()
    serializer_class = FlatsSerializer


class ManagerViewSets(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer