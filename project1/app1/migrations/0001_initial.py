# Generated by Django 4.1.7 on 2023-03-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DemoModel",
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
                ("name", models.CharField(max_length=40)),
                ("address", models.CharField(max_length=40)),
                ("phone", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]