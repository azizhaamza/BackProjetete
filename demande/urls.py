from django.urls import re_path
from django.urls.conf import include
from django.urls import path
from demande import views

urlpatterns = [
    path("dem", views.dem),
    path("print", views.print),
    path("show/<int:id>", views.show),
    path("edit/<int:id>", views.edit),
    path("update/<int:id>", views.update),
    path("delete/<int:id>", views.destroy),
    path("accept_demand/<int:id>", views.accept_demand),
    path("refuse_demand/<int:id>", views.refuse_demand),
]
