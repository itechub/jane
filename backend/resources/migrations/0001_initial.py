# Generated by Django 2.2 on 2019-10-23 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import resources.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Resource",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("filename", models.CharField(max_length=256)),
                (
                    "filetype",
                    models.CharField(
                        choices=[
                            ("IMAGE", "image"),
                            ("ATTACHMENT", "attachment"),
                        ],
                        default="IMAGE",
                        max_length=10,
                    ),
                ),
                (
                    "upload",
                    models.FileField(
                        upload_to=resources.models.resource_directory_path
                    ),
                ),
                (
                    "ctime",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="created at"
                    ),
                ),
                (
                    "mtime",
                    models.DateTimeField(
                        auto_now=True, verbose_name="created at"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resources",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="owner",
                    ),
                ),
            ],
        )
    ]
