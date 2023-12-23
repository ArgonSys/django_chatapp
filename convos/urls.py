from django.urls import path
from .views import ConvosView

app_name = "convos"


urlpatterns = [
    path("", ConvosView.as_view(), name="index")
]
