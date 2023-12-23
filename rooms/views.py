from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Room
from .forms import RoomForm


class RoomCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("users:login")
    redirect_field_name = "redirect_to"

    model = Room
    template_name = "rooms/new.html"
    form_class = RoomForm
