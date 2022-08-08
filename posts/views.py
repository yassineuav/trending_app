from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from .serializers import UserSerializer, InterestedInSerializer, RegisterUserSerializer, PostSerializer, \
    ProfileSerializer
from .models import InterestedIn, Post, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserAPIView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RegisterUserAPIView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterUserSerializer


class ProfileUserAPIView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfileSerializer
    # permission_classes = [permissions.IsAuthenticated]


class InterestedInViewSet(viewsets.ModelViewSet):
    queryset = InterestedIn.objects.all()
    serializer_class = InterestedInSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]


