from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class PointDeCollecte(models.Model):
    """
    Un point de collecte représente un magasin ou un producteur
    faisant de la vente en direct et appliquant un système de consigne
    pour réemploi de ses bouteilles. Il dispose d'un stock de casier
    qui doivent être collectés par L'INCASSABLE lorsqu'ils sont pleins.
    """

    nom = models.CharField(max_length=200)

    date_set_up = models.DateField(auto_now_add=True)

    adresse = models.CharField(max_length=200)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    nom_contact_1 = models.CharField(max_length=50, blank=True, null=True)
    nom_contact_2 = models.CharField(max_length=50, blank=True, null=True)

    email_contact_1 = models.EmailField(blank=True, null=True)
    email_contact_2 = models.EmailField(blank=True, null=True)

    telephone_1 = PhoneNumberField(blank=True, null=True)
    telephone_2 = PhoneNumberField(blank=True, null=True)

    stock_casier = models.IntegerField()

    def __str__(self):
        return self.nom
