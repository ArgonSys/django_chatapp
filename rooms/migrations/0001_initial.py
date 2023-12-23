# Generated by Django 5.0 on 2023-12-23 11:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="")),
                (
                    "members",
                    models.ManyToManyField(
                        to=settings.AUTH_USER_MODEL, verbose_name="members"
                    ),
                ),
            ],
            options={
                "verbose_name": "room",
                "verbose_name_plural": "rooms",
                "db_table": "rooms",
            },
        ),
    ]