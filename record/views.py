from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView

from record.models import Clients
from record.serializers import ClientsSerializer, ClientCreateSerializer


class ClientsAPIView(ListAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

    def get_queryset(self):
        return self.queryset.order_by('data')


class ClientsCreateAPIView(CreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientCreateSerializer

