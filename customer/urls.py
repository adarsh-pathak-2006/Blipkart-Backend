from django.urls import path
from customer.views import *

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('home/<slug:slug>/', IndividualProductView.as_view(), name='individual'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('cart/', CartView.as_view(), name='cart'),
]
