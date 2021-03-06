# Generated by Django 2.2 on 2019-06-17 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("articles", "0009_auto_20190617_2031")]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, unique=True)),
                ("description", models.CharField(max_length=256)),
                ("counts", models.PositiveIntegerField(default=0)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="TagMap",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "aid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tag_maps",
                        to="articles.Article",
                        verbose_name="article",
                    ),
                ),
                (
                    "tid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tag_maps",
                        to="tags.Tag",
                        verbose_name="tag",
                    ),
                ),
            ],
            options={"unique_together": {("aid", "tid")}},
        ),
        migrations.AddField(
            model_name="tag",
            name="articles",
            field=models.ManyToManyField(
                related_name="tags",
                through="tags.TagMap",
                to="articles.Article",
            ),
        ),
    ]
