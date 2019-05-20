# Generated by Django 2.1.4 on 2019-01-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=255, unique=True, verbose_name="邮箱"),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=32, null=True, unique=True, verbose_name="用户名"
                    ),
                ),
                (
                    "nickname",
                    models.CharField(max_length=32, null=True, verbose_name="昵称"),
                ),
                (
                    "real_name",
                    models.CharField(max_length=32, null=True, verbose_name="真实姓名"),
                ),
                ("date_of_birth", models.DateField(null=True, verbose_name="出生日期")),
                ("is_active", models.BooleanField(default=True, verbose_name="账户可用")),
                ("is_admin", models.BooleanField(default=False, verbose_name="管理员")),
                (
                    "joined",
                    models.DateTimeField(auto_now_add=True, verbose_name="加入时间"),
                ),
            ],
            options={"abstract": False},
        )
    ]
