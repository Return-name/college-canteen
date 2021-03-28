from django.urls import path
from foodfun import views

urlpatterns = [
    path("", views.index, name="index"),
]