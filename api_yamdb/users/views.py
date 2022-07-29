from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CreateUserSerializer, TokenObtainSerializer

User = get_user_model()


def send_registration_mail(user, token):
    send_mail(
        subject='Registration on YaMDb',
        message=(
            f'{user.username}, your verification code to receive a token: '
            f'{token}'
        ),
        from_email=None,
        recipient_list=[user.email],
        fail_silently=False,
    )


@api_view(['POST'])
def register_user(request):
    """Регистрация нового пользователя."""

    serializer = CreateUserSerializer(data=request.data)
    try:
        user = User.objects.get(
            username=request.data['username'],
            email=request.data['email'],
        )
    except Exception:
        user = None
    if not user:
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
    token = default_token_generator.make_token(user)
    send_registration_mail(user, token)
    return Response(request.data, status=status.HTTP_200_OK)


class TokenObtainView(TokenObtainPairView):
    """Получение токена."""

    serializer_class = TokenObtainSerializer
