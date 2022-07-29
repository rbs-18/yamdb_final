from django.urls import include, path

from .views import TokenObtainView, register_user

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('', include('djoser.urls.jwt')),
    path('signup/', register_user, name='registration'),
    path(
        'token/',
        TokenObtainView.as_view(),
        name='token_obtain_pair'
    ),
]
