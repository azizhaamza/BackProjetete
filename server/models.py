# appname/models.py
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    # Other fields

    def __str__(self):
        return self.username

    # class Demande_de_mission(models.Model):
    #     nom = models.CharField(max_length=200)
    #     prenom = models.CharField(max_length=200)
    #     plan = models.CharField(max_length=200)
    #     date_aller = models.DateTimeField(auto_now_add=True)
    #     date_retour = models.DateTimeField(auto_now_add=True)
    #     sujet_mission = models.TextField()
    #     accompagnant = models.TextField()
    #     reponse_admin = models.CharField(max_length=200)

    # def __str__(self):
    #    return self.nom
