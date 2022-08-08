from rest_framework import serializers
from .models import InterestedIn, Post, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterUserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = User.objects.update_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            city=validated_data['city'],
            state=validated_data['state'],
            zipCode=validated_data['zipCode'],
            bio=validated_data['bio'],
            imageUrl=validated_data['imageUrl']
        )
        return user

    class Meta:
        model = User
        fields = ['url', 'first_name', 'last_name', 'phone', 'city', 'state', 'zipCode', 'bio', 'imageUrl']


class InterestedInSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InterestedIn
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'description', 'content', 'imageUrl']
