from django.contrib import admin

from .models import PointDeCollecte

# Register your models here.


@admin.register(PointDeCollecte)
class PointDeCollecteAdmin(admin.ModelAdmin):
    list_display = ["nom", "adresse", "stock_casier"]
