from django.db import models
from django.utils import timezone


# Create your models here.


class Order(models.Model):
    id_user = models.IntegerField(default=0)
    id_demande = models.IntegerField(default=0)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    plan = models.CharField(max_length=200)
    date_aller = models.DateTimeField()
    date_retour = models.DateTimeField()
    sujet_mission = models.TextField()
    accompagnant = models.TextField()
    date_submit = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = "orders"
