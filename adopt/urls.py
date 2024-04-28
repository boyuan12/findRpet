from django.urls import path
from . import views

urlpatterns = [
    path('adoptable-animals', views.view_adoptable_animals, name='adoptable_animals'),
    path("search/", views.search_adoptable_animals, name="search_adoptable_animals")
]