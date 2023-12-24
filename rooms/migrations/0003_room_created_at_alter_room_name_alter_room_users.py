# Generated by Django 5.0 on 2023-12-24 13:17

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0002_rename_members_room_users"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=datetime.datetime.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="room",
            name="name",
            field=models.CharField(max_length=50, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="room",
            name="users",
            field=models.ManyToManyField(
                related_name="rooms",
                related_query_name="room",
                to=settings.AUTH_USER_MODEL,
                verbose_name="members",
            ),
        ),
    ]