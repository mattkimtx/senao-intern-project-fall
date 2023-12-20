from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
     path("", views.index, name="index"),
     path("login/", views.index, name="login"),
     path("signup/", views.signup, name="signup"),
]
