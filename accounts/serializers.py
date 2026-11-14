from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields=('username','email', 'password', 'rol')

    def create(self, validated_data):
        #fct create_user cripteaza automat parola cu hash (securizat)
        user=CustomUser.objects.create_user(
            username=validated_data['username'], #camp ogligatoriu
            email=validated_data.get('email', ''), #camp optional
            password=validated_data['password'],
            rol=validated_data.get('rol', 'user') #se atribuie automat user
        )
        return user