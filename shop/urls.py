from django.urls import path
from shop.views import *


urlpatterns = [
    path('', catalog),
    path('product_detail/<int:product_id>/',product_detail),
    path('Create_order/<int:product_id>/', create_order),
]



