from django.urls import path
from users.views import login_view, logout_view, signup_view
from fridge.views import add_ingredient

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("add_ingredient/", add_ingredient, name="add_ingredient"),
]