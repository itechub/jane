# Generated by Django 2.2 on 2019-06-12 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="motto",
            field=models.CharField(
                max_length=200, null=True, verbose_name="座右铭"
            ),
        )
    ]
