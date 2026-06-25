from django.urls import path
from staff.views import *

urlpatterns = [
    path('profile/', Profile_Admin_API.as_view(), name='profile'),
    path('profile/<slug:slug>/', Profile_individual_API.as_view(), name='profile_ind'),
    path('products/', Products_Admin_view.as_view(), name='products'),
    path('products/<slug:slug>/', Product_Admin_individual.as_view(), name='product_ind'),
]
