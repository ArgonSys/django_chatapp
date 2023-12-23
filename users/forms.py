from django.contrib.auth.forms import (
    AuthenticationForm as BaseAuthenticationForm,
    UserCreationForm as BaseUserCreationForm,
    UserChangeForm as BaseUserChangeForm,
    PasswordResetForm as BasePasswordResetForm,
    UsernameField,
)

from .models import User


class AuthenticationForm(BaseAuthenticationForm):
    pass


class UserCreationForm(BaseUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"autofocus": ""})

    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")



class UserChangeForm(BaseUserChangeForm):
    class Meta(BaseUserChangeForm.Meta):
        model = User

class PasswordResetForm(BasePasswordResetForm):
    pass
