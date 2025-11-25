from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.UserRegister.as_view(), name="register"),
    path("login/", views.Userlogin.as_view(), name="login")
]
