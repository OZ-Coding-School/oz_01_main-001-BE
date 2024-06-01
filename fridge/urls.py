from django.urls import path
from fridge.views import fridge_main, add_ingredient
from users.views import login_view

urlpatterns = [
    path('fridge_main/', fridge_main, name='fridge_main'),
    path('users/login/', login_view, name='login_view'),
    path('add_ingredient/', add_ingredient, name='add_ingredient'),
]