# Generated by Django 4.2.7 on 2023-11-18 20:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="publ_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
