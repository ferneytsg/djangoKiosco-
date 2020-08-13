from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =Account
        fields = ('__all__')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data.get('password'))
        print(user.set_password)
        print("Hola")
        user.save()
        return user