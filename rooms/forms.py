from django import forms


from .models import Room


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ("name", "users")
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "チャットルーム名を入力してください",
                "class": "chat__room_name chat-room-form__input",
            }),
        }
