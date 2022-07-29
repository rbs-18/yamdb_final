from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    """Сериализатор для создания пользователя."""

    class Meta:
        fields = ('email', 'username')
        model = User

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Using name "me" is prohibited!'
            )
        return value


class TokenObtainSerializer(TokenObtainPairSerializer):
    """Сериализатор для получения токена."""

    username_field = User.USERNAME_FIELD

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields['confirmation_code'] = serializers.CharField()

    def validate(self, attrs):
        current_user = get_object_or_404(
            User, username=attrs[self.username_field]
        )
        token = attrs['confirmation_code']
        if not default_token_generator.check_token(current_user, token):
            raise serializers.ValidationError(
                'Wrong confirmation code!'
            )
        refresh = RefreshToken.for_user(current_user)
        return {'token': str(refresh.access_token)}
