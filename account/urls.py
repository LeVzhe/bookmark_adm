from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(http_method_names=["post", "get"]),
        name="logout",
    ),
    path("", views.dashboard, name="dashboard"),
]
