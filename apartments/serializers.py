from rest_framework import serializers
from .models import Category,Status,Clients,Flats,Manager


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class FlatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flats
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'