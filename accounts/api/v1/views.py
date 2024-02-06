from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.serializers import SocialLoginSerializer
from dj_rest_auth.registration.views import RegisterView, SocialLoginView
from dj_rest_auth.views import LoginView as BaseLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


class EmailPasswordLoginAPIView(BaseLoginView):
    pass


class RegisterAPIView(RegisterView):
    pass


class GoogleLoginAPIView(SocialLoginView):
    serializer_class = SocialLoginSerializer
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
