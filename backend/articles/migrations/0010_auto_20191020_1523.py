# Generated by Django 2.2 on 2019-10-20 07:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [("articles", "0009_auto_20190617_2031")]

    operations = [
        migrations.AlterModelOptions(
            name="article", options={"ordering": ["is_sticky", "-mtime"]}
        ),
        migrations.RemoveField(model_name="article", name="created"),
        migrations.RemoveField(model_name="article", name="last_modified"),
        migrations.AddField(
            model_name="article",
            name="ctime",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="posted at",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="article",
            name="mtime",
            field=models.DateTimeField(
                auto_now=True, verbose_name="updated at"
            ),
        ),
    ]
