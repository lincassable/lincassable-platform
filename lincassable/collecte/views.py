from django.shortcuts import render
from .models import PointDeCollecte


def index(request):
    point_de_collectes = PointDeCollecte.objects.all()
    context = {"point_de_collectes": point_de_collectes}
    return render(request, "collecte/index.html", context)
