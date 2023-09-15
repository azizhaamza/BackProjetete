from rest_framework import serializers
from django.contrib.auth.models import User

# from .models import Demande_de_mission


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ["id", "username", "password", "email", "is_staff"]


# class Demande_de_mission(serializers.ModelSerializer):
#     class Meta(object):
#         model = Demande_de_mission
#         fields = ["id", "username", "password", "email", "is_staff"]
