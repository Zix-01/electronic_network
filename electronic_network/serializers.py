from rest_framework import serializers

from electronic_network.models import NetworkNode, Factory, RetailNetwork, Entrepreneur


class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = '__all__'


class FactorySerializer(serializers.ModelSerializer):
    class Meta(NetworkNodeSerializer.Meta):
        model = Factory


class RetailNetworkSerializer(serializers.ModelSerializer):
    class Meta(NetworkNodeSerializer.Meta):
        model = RetailNetwork


class EntrepreneurSerializer(serializers.ModelSerializer):
    class Meta(NetworkNodeSerializer.Meta):
        model = Entrepreneur
