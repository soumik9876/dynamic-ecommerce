from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class ProductView(TemplateView):
    template_name = 'shop/product_list.html'
