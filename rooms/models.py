from django.db import models
from django.utils.translation import gettext_lazy as _

class Room(models.Model):
    name = models.CharField(_(""), max_length=50)
    users = models.ManyToManyField("users.User", verbose_name=_("members"))

    class Meta:
        verbose_name = _("room")
        verbose_name_plural = _("rooms")
        db_table = "rooms"
