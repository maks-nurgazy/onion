from rest_framework import viewsets, permissions

from api.serializers import UserSerializer
from user.models import Users


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
