from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.contrib.auth.views import(
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView
)


from .forms import UserCreationForm, UserChangeForm, AuthenticationForm


class SignupView(CreateView):
    template_name = "users/signup.html"
    form_class = UserCreationForm
    success_url = "/"

class LoginView(BaseLoginView):
    template_name = "users/login.html"
    form_class = AuthenticationForm
    success_url = "/"

class LogoutView(BaseLogoutView):
    pass
