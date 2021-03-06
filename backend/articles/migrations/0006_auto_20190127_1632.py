# Generated by Django 2.1.4 on 2019-01-27 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("articles", "0005_auto_20190126_1109")]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"ordering": ["is_stickied", "-last_modified"]},
        ),
        migrations.AddField(
            model_name="article",
            name="is_stickied",
            field=models.BooleanField(default=False),
        ),
    ]
