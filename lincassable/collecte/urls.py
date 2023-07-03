from django.urls import path
from collecte.views import (
    PointDeCollecteListView,
    PointDeCollecteCreateView,
    PointDeCollecteUpdateView,
    PointDeCollecteDeleteView,
)

from . import views

urlpatterns = [
    path(
        "pointdecollecte/list/",
        PointDeCollecteListView.as_view(),
        name="pointdecollecte_list",
    ),
    path(
        "pointdecollecte/add/",
        PointDeCollecteCreateView.as_view(),
        name="pointdecollecte_add",
    ),
    path(
        "pointdecollecte/<int:pk>/",
        PointDeCollecteUpdateView.as_view(),
        name="pointdecollecte_update",
    ),
    path(
        "pointdecollecte/<int:pk>/delete/",
        PointDeCollecteDeleteView.as_view(),
        name="pointdecollecte_delete",
    ),
]
