from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User
from rooms.models import Room


class Convo(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    post_by = models.ForeignKey(
        User,
        verbose_name=_("message"),
        on_delete=models.CASCADE
    )
    post_to = models.ForeignKey(
        Room,
        verbose_name=_("chat room"),
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "convos"
