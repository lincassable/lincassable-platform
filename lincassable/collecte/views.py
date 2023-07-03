from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import PointDeCollecte
from django.urls import reverse_lazy


class PointDeCollecteListView(ListView):
    model = PointDeCollecte
    context_object_name = "points_de_collecte"


class PointDeCollecteCreateView(CreateView):
    model = PointDeCollecte
    fields = [
        "nom",
        "adresse",
        "latitude",
        "longitude",
        "nom_contact_1",
        "nom_contact_2",
        "email_contact_1",
        "email_contact_2",
        "telephone_1",
        "telephone_2",
        "stock_casier",
    ]
    success_url = reverse_lazy("pointdecollecte_list")


class PointDeCollecteUpdateView(UpdateView):
    model = PointDeCollecte
    fields = [
        "nom",
        "adresse",
        "latitude",
        "longitude",
        "nom_contact_1",
        "nom_contact_2",
        "email_contact_1",
        "email_contact_2",
        "telephone_1",
        "telephone_2",
        "stock_casier",
    ]
    success_url = reverse_lazy("pointdecollecte_list")


class PointDeCollecteDeleteView(DeleteView):
    model = PointDeCollecte
    success_url = reverse_lazy("pointdecollecte_list")


def add_point_de_collecte(request):
    return render(request, "collecte/add-point-de-collecte.html")
