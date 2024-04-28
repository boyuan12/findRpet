from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name='register'),
    path("register_pa/", views.register_pa),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout')
]