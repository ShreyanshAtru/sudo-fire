from rest_framework import  serializers
from api.models import User, Customer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'email', 'mobile']

    def create(self, validated_data):
        obj = User.objects.create(**validated_data)
        return obj 