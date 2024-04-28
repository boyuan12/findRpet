from django.urls import path
from . import views

urlpatterns = [
    path("", views.scroll_page, name='scroll_page'),
    path("pet-profile/<int:pk>", views.pet_page, name='pet_profile'),
    path("make-post", views.make_post, name='post_pet'),
    path("found/<int:pk>", views.found)
]