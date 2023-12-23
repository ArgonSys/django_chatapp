from django.urls import path

from .views import SignupView, LoginView, LogoutView, PasswordResetView


app_name = "users"

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password/", PasswordResetView.as_view(), name="password_reset"),
]
