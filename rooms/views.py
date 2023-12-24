from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Room
from .forms import RoomForm
from users.models import User

class RoomView(LoginRequiredMixin, View):
    login_url = reverse_lazy("users:login")
    redirect_field_name = "redirect_to"

    def get(self, request):
        rooms = request.user.rooms.all()
        return render(request, "rooms/index.html", { "rooms": rooms })



class RoomCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("users:login")
    redirect_field_name = "redirect_to"

    model = Room
    template_name = "rooms/new.html"
    form_class = RoomForm
    success_url = reverse_lazy("rooms:index")


    def get(self, request):
        form = RoomForm()
        users = User.objects.exclude(pk=request.user.pk)
        return render(request, self.template_name, {"form": form, "users": users})


    def post(self, request):
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            room.users.add(request.user)
            return redirect(self.success_url)
        else:
            users = User.objects.exclude(pk=request.user.pk)
            return render(request, self.template_name, {"form": form, "users": users})
