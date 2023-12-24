from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from PIL import Image
import os

from .models import Convo
from .forms import ConvoForm

from rooms.models import Room


class ConvosView(LoginRequiredMixin, View):
    login_url = reverse_lazy("users:login")
    redirect_field_name = "redirect_to"

    form_class = ConvoForm


    def get(self, request, room_pk):
        room = Room.objects.get(pk=room_pk)
        if not request.user in room.users.all():
            return redirect("rooms:index")
        form = ConvoForm
        convos = room.convo_set.prefetch_related("post_by")
        return render(request, "convos/index.html", {"form": form, "convos": convos, "room": room, "rooms": request.user.rooms.all()})


    def post(self, request, room_pk):
        room = Room.objects.get(pk=room_pk)
        if not request.user in room.users.all():
            return redirect("rooms:index")
        form = ConvoForm(request.POST)
        if form.is_valid:
            convo = Convo()
            convo.text = request.POST.get("text")
            convo.image = request.FILES.get("image")
            convo.post_by = request.user
            convo.post_to = room
            convo.save()
            resize_image(convo.image.url)
            return redirect("convos:index", room_pk=room_pk)
        return render(request, "convos/index.html", {"form": form, "room": room, "rooms": request.user.rooms.all()})


def resize_image(url):
    url = url.lstrip("/")
    with Image.open(url) as img_file:
        os.remove(url)
        img_resized = img_file.resize((500, 500))
        img_resized.save(url)
