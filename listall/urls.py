from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('category/', views.category_index, name='category_index'),
        path('new_additions/', views.new_addition, name='new_addition'),
        ]
