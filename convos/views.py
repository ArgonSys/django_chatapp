from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from django.http import HttpResponse


class ConvosView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(b"ConvosView")
