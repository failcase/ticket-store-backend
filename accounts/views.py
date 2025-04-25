from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions

from .models import CustomUser
from .serializers import UserProfileSerializer, CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            # Только владелец профиля может редактировать
            return [permissions.IsAuthenticated(), IsOwner()]
        return [permissions.AllowAny()]


class IsOwner(permissions.BasePermission):
    """
    Разрешает редактировать только если пользователь сам владелец профиля
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user
