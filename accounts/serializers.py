from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from accounts.models import CustomUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')
        read_only_fields = ('username',)

class CustomRegisterSerializer(RegisterSerializer):
    # новые поля
    first_name = serializers.CharField(required=True)
    last_name  = serializers.CharField(required=False)

    def get_cleaned_data(self):
        """
        Возвращаем все поля, которые allauth будет
        записывать в модель пользователя.
        """
        data = super().get_cleaned_data()
        data['first_name'] = self.validated_data.get('first_name', '')
        data['last_name']  = self.validated_data.get('last_name', '')
        return data