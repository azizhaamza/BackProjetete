from django.db import models
from django.utils import timezone


class Demande(models.Model):
    id_user = models.IntegerField(default=0)
    date_submit = models.DateTimeField(default=timezone.now)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    plan = models.CharField(max_length=200)
    date_aller = models.DateTimeField()
    date_retour = models.DateTimeField()
    sujet_mission = models.TextField()
    accompagnant = models.TextField()
    reponse_admin = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = "demande"
