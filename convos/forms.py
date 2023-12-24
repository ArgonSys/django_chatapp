from django import forms

from .models import Convo


class ConvoForm(forms.ModelForm):
    class Meta:
        model = Convo
        fields = ("text", "image")
        widgets = {
            "text": forms.TextInput(attrs={
                "class": "text-form",
                "placeholder": "type a message",
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "hidden",
            }),
        }
