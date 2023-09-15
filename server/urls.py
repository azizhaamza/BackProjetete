from django.urls import re_path
from . import views
from django.urls.conf import include
from django.urls import path

urlpatterns = [
    re_path("login", views.login, name="login"),
    re_path("users", views.get_users, name="get_users"),
    re_path("signup", views.signup),
    re_path("test_token", views.test_token),
    path("", include("demande.urls")),
    path("", include("orders.urls")),
]
