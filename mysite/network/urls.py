from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("results/", views.SearchResultsView.as_view(), name="results"),
    #path("", views.SearchResultsView.as_view(), name="index"),
]
