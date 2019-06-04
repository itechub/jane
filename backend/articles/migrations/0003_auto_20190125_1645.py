# Generated by Django 2.1.4 on 2019-01-25 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("articles", "0002_auto_20190125_1632"),
    ]

    operations = [
        migrations.RenameModel(old_name="Post", new_name="Article"),
        migrations.RemoveField(model_name="tagmap", name="pid"),
        migrations.AddField(
            model_name="tagmap",
            name="aid",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="articles",
                to="articles.Article",
                verbose_name="article",
            ),
            preserve_default=False,
        ),
    ]
