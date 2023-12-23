from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import(
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView,
    PasswordResetView as BasePasswordResetView
)
from django.urls import reverse_lazy

from .forms import(
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    PasswordResetForm
)
from .models import User


class SignupView(CreateView):
    template_name = "users/signup.html"
    form_class = UserCreationForm
    extra_context = {"from_signup": True}
    success_url = "/"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("top")
        return super().get(request,*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("top")
        return super().post(request,*args, **kwargs)


    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return response


class LoginView(BaseLoginView):
    redirect_authenticated_user = True
    template_name = "users/login.html"
    form_class = AuthenticationForm
    extra_context = {"from_login": True}
    success_url = "/"


class LogoutView(LoginRequiredMixin, BaseLogoutView):
    login_url = reverse_lazy("users:login")
    redirect_field_name = "redirect_to"


class PasswordResetView(LoginRequiredMixin, BasePasswordResetView):
    login_url = reverse_lazy("users:login")
    redirect_field_name = "redirect_to"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("users:login")
    redirect_field_name = "redirect_to"

    model = User
    template_name = "users/edit.html"
    form_class = UserChangeForm
    success_url = "/"
