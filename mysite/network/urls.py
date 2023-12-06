from django.urls import path

from . import views

app_name = "network"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # path("results/", views.findEvent, name="results"),
    path("results/", views.SearchResultsView.as_view(), name="results"),
    #path("", views.SearchResultsView.as_view(), name="index"),
]

