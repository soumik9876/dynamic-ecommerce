from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.api.v1.views import EmailPasswordLoginAPIView, GoogleLoginAPIView, RegisterAPIView

urlpatterns = [
    path('login/', EmailPasswordLoginAPIView.as_view(), name='login'),
    path('login/google/', GoogleLoginAPIView.as_view(), name='login-google'),
    path('register/', include('dj_rest_auth.registration.urls')),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
