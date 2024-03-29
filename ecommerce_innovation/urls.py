"""ecommerce_innovation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ecommerce_innovation.settings import ENV_TYPE, MEDIA_URL, MEDIA_ROOT

api_url_patterns = (
    [
        path('accounts/v1/', include('accounts.api.v1.urls')),
        path('shop/v1/', include('shop.api.v1.urls')),
    ]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns)),
    path('', include('shop.urls'))
]

if ENV_TYPE == 'DEVELOPMENT':
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

