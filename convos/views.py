from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse



class ConvosView(LoginRequiredMixin, View):
    login_url = "/users/login/"
    redirect_field_name = "redirect_to"

    def get(self, request, *args, **kwargs):
        return render(request, "convos/index.html")
