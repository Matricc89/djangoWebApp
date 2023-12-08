

from django.urls import path
from . import views

app_name = "consesionario"

urlpatterns = [
    path("", views.home, name='index'),
    path("customers/", views.customers_view, name='customers'),
    path("garages/", views.garages_view, name='garages'),
    path("cars/", views.cars_view, name='cars'),
    path("list/", views.list, name='list'),
    path("search/", views.search_view, name='search'),


    

]
