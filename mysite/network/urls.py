from django.urls import path
from . import views

app_name = "network"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("results/", views.SearchResultsView.as_view(), name="results"),
    path("mongodb/", views.my_view, name="mongo"),
    path("dbresults/", views.mongo_dbs, name="dbresults")
]

