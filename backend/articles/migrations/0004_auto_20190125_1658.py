# Generated by Django 2.1.4 on 2019-01-25 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("articles", "0003_auto_20190125_1645")]

    operations = [
        migrations.AlterUniqueTogether(
            name="tagmap", unique_together={("aid", "tid")}
        )
    ]
