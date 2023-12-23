from django.contrib.auth.forms import (
    AuthenticationForm as BaseAuthenticationForm,
    UserCreationForm as BaseUserCreationForm,
    UserChangeForm as BaseUserChangeForm,
    PasswordResetForm as BasePasswordResetForm
)

from .models import User


class AuthenticationForm(BaseAuthenticationForm):
    pass

class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User


class UserChangeForm(BaseUserChangeForm):
    class Meta(BaseUserChangeForm.Meta):
        model = User

class PasswordResetForm(BasePasswordResetForm):
    pass
