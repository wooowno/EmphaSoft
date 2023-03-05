from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializers import UserSerializer


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserSerializer
