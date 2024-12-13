# from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    # ###
    # ###
    # path(
    #     "password-change/",
    #     auth_views.PasswordChangeView.as_view(),
    #     name="password_change",
    # ),
    # path(
    #     "password-change/done/",
    #     auth_views.PasswordChangeDoneView.as_view(),
    #     name="password_change_done",
    # ),
    # ###
    # path(
    #     "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    # ),
    # path(
    #     "password_reset/done/",
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "password_reset/<uidb64>/<token>/",
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "password_reset/complete/",
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
    ###
    path("login/", views.MyLoginView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("", views.dashboard, name="dashboard"),
]
