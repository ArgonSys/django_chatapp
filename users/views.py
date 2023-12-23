from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.contrib.auth.views import(
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView,
    PasswordResetView as BasePasswordResetView
)


from .forms import(
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    PasswordResetForm
)


class SignupView(CreateView):
    template_name = "users/signup.html"
    form_class = UserCreationForm
    success_url = "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return response


class LoginView(BaseLoginView):
    template_name = "users/login.html"
    form_class = AuthenticationForm
    success_url = "/"


class LogoutView(BaseLogoutView):
    pass


class PasswordResetView(BasePasswordResetView):
    pass
