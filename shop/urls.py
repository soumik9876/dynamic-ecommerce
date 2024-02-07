from django.urls import path

from shop.views import ProductView

urlpatterns = [
    path('', ProductView.as_view(), name='products'),
]
