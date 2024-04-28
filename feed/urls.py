from django.urls import path
from . import views

urlpatterns = [
    path("map/", views.view_map, name='stray_map'),
    path("add/", views.add_location, name='add_stray'),
    path("fetch-locations/", views.fetch_locations)
]