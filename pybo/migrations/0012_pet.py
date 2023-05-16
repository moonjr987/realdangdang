# Generated by Django 4.1.5 on 2023-03-19 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pybo", "0011_alter_expert_answer_question"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pet",
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
                ("photo", models.ImageField(upload_to="photos/%Y/%m/%d/")),
            ],
        ),
    ]