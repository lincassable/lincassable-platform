from django.db import models

# Create your models here.


class PointDeCollecte(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    stock_casier = models.IntegerField()

    def __str__(self):
        return self.nom
