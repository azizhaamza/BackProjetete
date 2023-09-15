from django.urls import re_path
from django.urls.conf import include
from django.urls import path
from orders import views

urlpatterns = [
    path("ord", views.ord),
    path("show", views.show),
    path("edit/<int:id>", views.edit),
    path("update/<int:id>", views.update),
    path("delete/<int:id>", views.destroy),
]
