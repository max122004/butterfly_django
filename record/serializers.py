from rest_framework import serializers

from record.models import Clients, Masters


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masters
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = Clients
        fields = ['name', 'phone', 'data', 'time', 'service']


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'